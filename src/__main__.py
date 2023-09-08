from struct import *
from arch.riscv.isa.instruction import Instruction
from arch.riscv.isa.decoder import RiscVDecoder
from arch.riscv.isa.encoder import RiscVEncoder
from elf import ElfHeader
from elf.sections import SectionHeader
from elf.segments import ProgramHeader
from enums.elf import BitFormat, MachineType, ProgramFlags, ProgramType
import shutil

import pdb

outfile = './hello'
filename = './output'
# filename = './hello'
# outfile = './output'
# filename = './philosophers_dinner_(2)'
# filename = './riscv32-unknown-elf-gcc' 

# shutil.copyfile(filename, outfile)

with open(filename, 'rb+') as fp:
    header = ElfHeader()
    
    header.parse(fp)
    assert MachineType(header['e_machine']) == MachineType.RISCV
    assert BitFormat(header['e_bit_format']) == BitFormat.BIT_64
    
    program_table_offset = header['e_phoff']
    
    print(f'Program table offset: {program_table_offset}')
    print(f'Program table size: {header["e_phentsize"]}')
    
    fp.seek(program_table_offset)
    
    # Parsing segments
    for i in range(header['e_phnum']):
        program_header = ProgramHeader(header)
        program_header.parse(fp)
        
        try:
            if ProgramType(program_header['p_type']) == ProgramType.LOAD and ProgramFlags(program_header['p_flags']) == ProgramFlags.RX:
                print('Found code segment')
                print(f"Permissions: {ProgramFlags(program_header['p_flags'])}")
                print(f"File offset: {program_header['p_offset']}")
                print(f"Virtual address: {program_header['p_vaddr']}")
                print(f"Physical address: {program_header['p_paddr']}")
                print(f"File size: {program_header['p_filesz']}")
        except ValueError as e:
            print("Unknown program type")
            
    # Parsing string table
    fp.seek(header['e_shoff'] + (header['e_shstrndx'] * header['e_shentsize']))
    string_table_header = SectionHeader(header)
    string_table_header.parse(fp)
    
    fp.seek(string_table_header['sh_offset'])
    str_section = fp.read(string_table_header['sh_size'])

    string_table = {}
    lastnull = 0
    for i, s in enumerate(str_section):
        if s == 0:
            string_table[lastnull] = str_section[lastnull:i]
            lastnull = i + 1
    
    # Parsing section table names
    section_table_index = header['e_shstrndx']
    
    for i in range(header['e_shnum']):
        fp.seek(header['e_shoff'] + (i * header['e_shentsize']))
        section_header = SectionHeader(header)
        section_header.parse(fp)
        
        name = string_table.get(section_header['sh_name'])

        if name is not None and name.decode('utf-8') == '.text':
            print('Found code section')
            print(f"File offset: {section_header['sh_offset']}")
            print(f"Virtual address: {section_header['sh_addr']}")
            print(f"Physical address: {section_header['sh_offset']}")
            print(f"File size: {section_header['sh_size']}")
            print(f"Section index: {i}")
            
            # Reads 32 bit for each instruction starting at sh_offset until shoffset + sh_size
            fp.seek(section_header['sh_offset'])
            j = 0
            
            total_instructions = 0
            total_decoded_instructions = 0
            total_target_instructions = 0
            
            while j < section_header['sh_size']:
                total_instructions += 1
                b_instruction = fp.read(4)
                instruction = int.from_bytes(b_instruction, 'little')
                print(f"{j:08x}: {instruction:08x}")
                
                try:
                    decoded_instruction = RiscVDecoder().decode(b_instruction)
                    # if (decoded_instruction.get('funct3') == '000' and decoded_instruction.opcodes[0] == '0010011'):
                    if (str(decoded_instruction) == "ADDI x0, x0, 0"):
                        decoded_instruction.set('imm', '1')
                        modified = RiscVEncoder().encode(decoded_instruction)
                        
                        position = fp.tell() - 4
                        
                        with open(outfile, 'rb+') as out:
                            # shit not right
                            out.seek(position)
                            out.write(modified)
                        
                        
                    total_decoded_instructions += 1
                except ValueError:
                    # print(f"Unsupported {bin(int.from_bytes(b_instruction, 'little'))}")
                    pass
                
                # if (instruction == 65537):
                    # print(Instruction(b_instruction).decode())
                    # fp.seek(-4, 1)
                    # fp.write(b'\x00\x02\x00\x02')
                j += 4
            
            print(f"Total instructions: {total_instructions}")
            print(f"Total decoded instructions: {total_decoded_instructions}")
            print(f"Decoding ratio: {(total_decoded_instructions / total_instructions) * 100}.2f %")