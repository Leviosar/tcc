import click

from steganossaurus.elf.parser import parse
from steganossaurus.utils.logger import setup_logger
from typing import Literal

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option('--log-level', type=click.Choice(["debug", "info", "warning", "error", "critical"]))
def decode(file, log_level):
    setup_logger(log_level)
    
    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])
    message = ""
    char = ""
    
    for (decoded_instruction, address, pointer) in instruction_generator:
        rs1 = decoded_instruction.get('rs1')
        rs2 = decoded_instruction.get('rs2')
        
        # Can't decode if the registers are the same
        if rs1 == rs2:
            continue
        elif rs1 > rs2:
            char += "1"
        else:
            char += "0"
        
        if len(char) == 8:
            if char == "00000000":
                break
            else:
                message += chr(int(char, base=2))
                char = ""
    
    print("Message was decoded:")
    print(message)
    return
        