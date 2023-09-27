from io import BufferedReader
from pprint import pprint
from typing import Dict
from collections import OrderedDict
from steganossaurus.elf import ElfHeader

class SectionHeader:
    fields: Dict[str, 'SectionHeaderField'] = OrderedDict()
    
    def __init__(self, elf_header: ElfHeader):
        self.elf_header = elf_header
    
    def parse(self, file: BufferedReader):
        # 2 if 64 bits, 1 if 32 bits, 0 if invalid
        bit_len_flag = self.elf_header['e_bit_format']
        
        self.fields['sh_name'] = SectionHeaderField(4).parse(file)
        self.fields['sh_type'] = SectionHeaderField(4).parse(file)
        self.fields['sh_flags'] = SectionHeaderField(4 * bit_len_flag).parse(file)
        self.fields['sh_addr'] = SectionHeaderField(4 * bit_len_flag).parse(file)
        self.fields['sh_offset'] = SectionHeaderField(4 * bit_len_flag).parse(file)
        self.fields['sh_size'] = SectionHeaderField(4 * bit_len_flag).parse(file)
        self.fields['sh_link'] = SectionHeaderField(4).parse(file)
        self.fields['sh_info'] = SectionHeaderField(4).parse(file)
        self.fields['sh_addralign'] = SectionHeaderField(4 * bit_len_flag).parse(file)
        self.fields['sh_entsize'] = SectionHeaderField(4 * bit_len_flag).parse(file)
    
    def __getitem__(self, key: str):
        return self.fields[key].value
    
class SectionHeaderField:
    value: int
    bvalue: bytes
    
    def __init__(self, size: int):
        self.size = size
        
    def parse(self, fp: BufferedReader):
        self.bvalue = fp.read(self.size)
        self.value = int.from_bytes(self.bvalue, 'little')
        return self
    
    def __repr__(self) -> str:
        return f'SectionHeaderField({self.value})'