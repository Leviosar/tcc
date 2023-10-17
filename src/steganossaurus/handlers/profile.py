import click
import os

from steganossaurus.elf.parser import parse
from steganossaurus.utils.logger import setup_logger
from typing import Literal

import logging

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-o", '--output', type=click.Path())
@click.option('--log-level', type=click.Choice(["debug", "info", "warning", "error", "critical"]))
def profile(file, output, log_level):
    setup_logger(log_level)
    
    capacity = 0    
    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])
    natural_bits = [0, 0]
    
    for (decoded_instruction, address, pointer) in instruction_generator:
        rs1 = decoded_instruction.get('rs1')
        rs2 = decoded_instruction.get('rs2')
        
        # Can't encode if the registers are the same
        if rs1 == rs2:
            continue
        elif rs1 > rs2:
            natural_bits[1] += 1
        else:
            natural_bits[0] += 1
        
        if output is not None:
            with open(output, 'a') as fp:
                fp.write(f"Candidate Instruction: {str(decoded_instruction)}\n")
                
        capacity += 1
    
    print(f"File size (Bytes): {os.path.getsize(file)}")
    print(f"Encoding capacity (Bytes): {(capacity // 8) - 1}")
    print(f"Encoding capacity (Characters): {(capacity // 8 - 1)}")
    print(f"Natural 0 encoded bits: {natural_bits[0]}")
    print(f"Natural 1 encoded bits: {natural_bits[1]}")
    return
        