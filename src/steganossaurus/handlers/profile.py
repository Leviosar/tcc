import click
import os

from steganossaurus.elf.parser import parse

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-o", '--output', type=click.Path())
def profile(file, output):
    capacity = 0    
    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])
    
    for (decoded_instruction, address, pointer) in instruction_generator:
        rs1 = decoded_instruction.get('rs1')
        rs2 = decoded_instruction.get('rs2')
        
        # Can't encode if the registers are the same
        if rs1 == rs2:
            continue
        
        if output is not None:
            with open(output, 'a') as fp:
                fp.write(f"Candidate Instruction: {str(decoded_instruction)}\n")
                
        capacity += 1
        
    print(f"File size (Bytes): {os.path.getsize(file)}")
    print(f"Encoding capacity (Bytes): {(capacity // 8) - 1}")
    print(f"Encoding capacity (Characters): {(capacity // 8 - 1)}")
    return
        