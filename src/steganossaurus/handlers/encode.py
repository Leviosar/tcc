import click
import shutil

from steganossaurus.elf.parser import parse
from steganossaurus.arch.riscv.isa.encoder import RiscVEncoder
from steganossaurus.utils.logger import setup_logger
from steganossaurus.utils.crypto import encrypt
from typing import Literal


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.argument("message")
@click.option("-o", "--output", type=click.Path(), help="Path to output file, created if not exists.")
@click.option(
    "--log-level", type=click.Choice(["debug", "info", "warning", "error", "critical"]),
    help="Level of data to de logged."
)
@click.password_option(help="Password used to encrypt the message.")
def encode(
    file: str,
    message: str,
    output: str,
    log_level: Literal["debug", "info", "warning", "error", "critical"],
    password: str,
):
    """Embeds a message into the given FILE, encrypting it with a required password."""
    setup_logger(log_level)

    if output is not None:
        shutil.copy(file, output)

    # Encrypts the plaintext message using AES with OFB mode to add pseudorandom distribution to each char
    encrypted_message = encrypt(message.encode("ascii"), password)

    # Splits message into ascii codepoints list
    encrypted_message = list(encrypted_message)
    splitted_message = [
        bin(int(char)).replace("0b", "").rjust(8, "0") for char in encrypted_message
    ]

    # Adding a nul ascii char at message end
    message = "".join(splitted_message) + "00000000"

    message_index = 0

    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])

    for decoded_instruction, address, pointer in instruction_generator:
        rs1 = decoded_instruction.get("rs1")
        rs2 = decoded_instruction.get("rs2")

        # Can't encode if the registers are the same
        if rs1 == rs2:
            continue

        # We encode 1 as rs1 > rs2
        if message[message_index] == "1":
            if not (rs1 > rs2):
                aux = rs1
                decoded_instruction.set("rs1", rs2)
                decoded_instruction.set("rs2", aux)
        # And bit 0 as rs1 < rs2
        else:
            if not (rs1 < rs2):
                aux = rs1
                decoded_instruction.set("rs1", rs2)
                decoded_instruction.set("rs2", aux)

        if output is not None:
            modified = RiscVEncoder().encode(decoded_instruction)
            with open(output, "rb+") as fp:
                fp.seek(pointer)
                fp.write(modified)

        message_index += 1

        if message_index >= len(message):
            break

    if message_index >= len(message):
        print(f"Message was encoded at {output}")
    else:
        print(
            "File doesn't have enough encoding capacity. To check the needed capacity for a given message use the `profile` command."
        )
    return
