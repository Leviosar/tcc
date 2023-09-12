from io import BufferedReader
from pprint import pprint
from typing import Dict
from collections import OrderedDict
from steganossaurus.elf import ElfHeader

from steganossaurus.enums.elf import ABI, BitFormat, ElfType, Endianess, MachineType

class ProgramHeader:
    fields: Dict[str, 'ProgramHeaderField'] = OrderedDict()
    
    def __init__(self, elf_header: ElfHeader):
        self.elf_header = elf_header
    
    def parse(self, file: BufferedReader):
        self.fields['p_type'] = ProgramHeaderField(4).parse(file)
        
        # 2 if 64 bits, 1 if 32 bits, 0 if invalid
        bit_len_flag = self.elf_header['e_bit_format']
        
        if BitFormat(bit_len_flag) == BitFormat.BIT_64:
            self.fields['p_flags'] = ProgramHeaderField(4).parse(file)
        
        self.fields['p_offset'] = ProgramHeaderField(4 * bit_len_flag).parse(file)
        self.fields['p_vaddr']  = ProgramHeaderField(4 * bit_len_flag).parse(file)
        self.fields['p_paddr']  = ProgramHeaderField(4 * bit_len_flag).parse(file)
        self.fields['p_filesz'] = ProgramHeaderField(4 * bit_len_flag).parse(file)
        self.fields['p_memsz']  = ProgramHeaderField(4 * bit_len_flag).parse(file)
        
        if BitFormat(bit_len_flag) == BitFormat.BIT_32:
            self.fields['p_flags'] = ProgramHeaderField(4).parse(file)
        
        self.fields['p_align'] = ProgramHeaderField(4 * bit_len_flag).parse(file)
    
    def __getitem__(self, key: str):
        return self.fields[key].value
    
class ProgramHeaderField:
    value: int
    bvalue: bytes
    
    def __init__(self, size: int):
        self.size = size
        
    def parse(self, fp: BufferedReader):
        self.bvalue = fp.read(self.size)
        self.value = int.from_bytes(self.bvalue, 'little')
        return self
    
    def __repr__(self) -> str:
        return f'ProgramHeaderField({self.value})'