# from struct import *
from typing import Generator, Tuple

from steganossaurus.arch.riscv.isa.decoder import RiscVDecoder
from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction
from steganossaurus.elf import ElfHeader
from steganossaurus.elf.sections import SectionHeader
from steganossaurus.elf.segments import ProgramHeader
from steganossaurus.elf.string_table import StringTable
from steganossaurus.enums.elf import BitFormat, MachineType, ProgramFlags, ProgramType, SectionType
import logging

def parse(filename, supported = ["*"], debug = False) -> Generator[Tuple[Instruction, int, int], None, None]:
    with open(filename, 'rb+') as fp:
        header = ElfHeader()
        
        header.parse(fp)
        
        assert MachineType(header['e_machine']) == MachineType.RISCV
        assert BitFormat(header['e_bit_format']) == BitFormat.BIT_64
        
        program_table_offset = header['e_phoff']
        
        logging.debug(f'Program table offset: {program_table_offset}')
        logging.debug(f'Program table size: {header["e_phentsize"]}')
        
        fp.seek(program_table_offset)
        
        # Parsing segments
        for i in range(header['e_phnum']):
            program_header = ProgramHeader(header)
            program_header.parse(fp)
            
            try:
                if ProgramType(program_header['p_type']) == ProgramType.LOAD and ProgramFlags(program_header['p_flags']) == ProgramFlags.RX:
                    logging.debug(f"Found code segment")
                    logging.debug(f"Permissions: {ProgramFlags(program_header['p_flags'])}")
                    logging.debug(f"File offset: {program_header['p_offset']}")
                    logging.debug(f"Virtual address: {program_header['p_vaddr']}")
                    logging.debug(f"Physical address: {program_header['p_paddr']}")
                    logging.debug(f"File size: {program_header['p_filesz']}")
            except ValueError as e:
                logging.debug("Unknown program type")
                
        # Parsing string table
        fp.seek(header['e_shoff'] + (header['e_shstrndx'] * header['e_shentsize']))
        string_table_header = SectionHeader(header)
        string_table_header.parse(fp)
        
        string_table = StringTable(fp, string_table_header['sh_offset'], string_table_header['sh_size'])
        
        # Parsing section table names
        # section_table_index = header['e_shstrndx']
        
        for i in range(header['e_shnum']):
            fp.seek(header['e_shoff'] + (i * header['e_shentsize']))
            section_header = SectionHeader(header)
            section_header.parse(fp)
            
            name = string_table.get(section_header['sh_name'])

            logging.debug(f"Found Section")
            logging.debug(f"-------------")
            logging.debug(f"Section index: {i}")
            logging.debug(f"Section name: {name}")
            logging.debug(f"Section type: {SectionType.from_int(section_header['sh_type'])}")
            logging.debug(f"File offset: {section_header['sh_offset']}")
            logging.debug(f"Virtual address: {section_header['sh_addr']}")
            logging.debug(f"Physical address: {section_header['sh_offset']}")
            logging.debug(f"File size: {section_header['sh_size']}")
            logging.debug(f"-------------")
                
            if name is not None and name.decode('utf-8') == '.text':
                
                # Reads 32 bit for each instruction starting at sh_offset until shoffset + sh_size
                fp.seek(section_header['sh_offset'])
                j = 0
                
                total_instructions = 0
                total_decoded_instructions = 0
                
                while j < section_header['sh_size']:
                    total_instructions += 1
                    
                    try:
                        decoded_instruction, size = RiscVDecoder().decode(fp)
                        
                        logging.debug(f"{j:08x} : {decoded_instruction}")
                            
                        j += size
                        
                        if decoded_instruction is None:
                            continue
                        
                        if decoded_instruction.mne() in supported or "*" in supported:
                            yield (decoded_instruction, j, fp.tell() - 4)
                            
                        total_decoded_instructions += 1
                    except ValueError as e:
                        logging.debug(f"{j:08x}: {e}")
                        pass
                    
                    j += 4
                
                logging.debug(f"Total instructions: {total_instructions}")
                logging.debug(f"Total decoded instructions: {total_decoded_instructions}")
                logging.debug(f"Decoding ratio: {(total_decoded_instructions / total_instructions) * 100}.2f %")