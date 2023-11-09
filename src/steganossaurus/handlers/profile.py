import click
import os

from steganossaurus.elf.parser import parse
from steganossaurus.utils.logger import setup_logger
from steganossaurus.utils.crypto import encrypt
from typing import Literal, Union

import logging


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-o", "--output", type=click.Path())
@click.option(
    "--log-level", type=click.Choice(["debug", "info", "warning", "error", "critical"])
)
@click.option("--message")
def profile(file: str, output: str, log_level: Literal["debug", "info", "warning", "error", "critical"], message: Union[str, None] = None):
    """Runs a profile for binary steganography on a given file

    Args:
        file str: path to the binary file
        output str: path to output file
        log_level Literal["debug", "info", "warning", "error", "critical"]: Level for log messages.
        message (Union[str, None], optional): message to check if fits on file or not. Defaults to None.

    Returns:
        (int, int, (int, int)): tuple containing (filesize, encoding capacity in bits, (natural encoded 0 bits, natural encoded 1 bits))
    """
    setup_logger(log_level)

    capacity: int = 0
    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])
    natural_bits = [0, 0]

    for decoded_instruction, address, pointer in instruction_generator:
        rs1 = decoded_instruction.get("rs1")
        rs2 = decoded_instruction.get("rs2")

        # Can't encode if the registers are the same
        if rs1 == rs2:
            continue
        elif rs1 > rs2:
            natural_bits[1] += 1
        else:
            natural_bits[0] += 1

        if output is not None:
            with open(output, "a") as fp:
                fp.write(f"Candidate Instruction: {str(decoded_instruction)}\n")

        capacity += 1

    logging.info(f"File size (in Bytes): {os.path.getsize(file)}")
    logging.info(f"Encoding capacity (in Bytes): {(capacity // 8) - 1}")
    logging.info(f"KB per bit: {((os.path.getsize(file) / 1024) // capacity)}")

    if message is not None:
        # Password here doesn't matter, the message is only used for profiling
        encrypted_message = encrypt(message.encode("ascii"), "big_bad_wolf")

        # Splits message into ascii codepoints list
        encrypted_message = list(encrypted_message)

        print(f"Message size (encrypted, in Bytes): {len(encrypted_message) + 1}")

    return (
        os.path.getsize(file),
        capacity,
        (natural_bits[0], natural_bits[1])
    )
