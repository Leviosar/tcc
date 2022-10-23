from io import BufferedReader
from pprint import pprint
from typing import Dict
from collections import OrderedDict

from enums.elf import ABI, BitFormat, ElfType, Endianess, MachineType

BIT_64 = 1
BIT_32 = 2

class Elf:
    def __init__(self):
        pass

class ElfHeader:
    fields: Dict[str, 'ElfHeaderField'] = OrderedDict()
    
    def parse(self, file: BufferedReader):
        self.fields['e_magic'] = ElfHeaderField(4).parse(file)
        self.fields['e_bit_format'] = ElfHeaderField(1).parse(file)
        self.fields['e_endianness'] = ElfHeaderField(1).parse(file)
        self.fields['e_elf_version'] = ElfHeaderField(1).parse(file)
        self.fields['e_os_abi'] = ElfHeaderField(1).parse(file)
        self.fields['e_abi_version'] = ElfHeaderField(1).parse(file)
        self.fields['e_padding'] = ElfHeaderField(7).parse(file)
        self.fields['e_type'] = ElfHeaderField(2).parse(file)
        self.fields['e_machine'] = ElfHeaderField(2).parse(file)
        self.fields['e_version'] = ElfHeaderField(4).parse(file)
        self.fields['e_entry'] = ElfHeaderField(4 * self.fields['e_bit_format'].value).parse(file)
        self.fields['e_phoff'] = ElfHeaderField(4 * self.fields['e_bit_format'].value).parse(file)
        self.fields['e_shoff'] = ElfHeaderField(4 * self.fields['e_bit_format'].value).parse(file)
        self.fields['e_flags'] = ElfHeaderField(4).parse(file)
        self.fields['e_ehsize'] = ElfHeaderField(2).parse(file)
        self.fields['e_phentsize'] = ElfHeaderField(2).parse(file)
        self.fields['e_phnum'] = ElfHeaderField(2).parse(file)
        self.fields['e_shentsize'] = ElfHeaderField(2).parse(file)
        self.fields['e_shnum'] = ElfHeaderField(2).parse(file)
        self.fields['e_shstrndx'] = ElfHeaderField(2).parse(file)
    
    def __getitem__(self, key: str):
        return self.fields[key].value
    
class ElfHeaderField:
    value: int
    bvalue: bytes
    
    def __init__(self, size: int):
        self.size = size
        
    def parse(self, fp: BufferedReader):
        self.bvalue = fp.read(self.size)
        self.value = int.from_bytes(self.bvalue, 'little')
        return self
    
    def __repr__(self) -> str:
        return f'ElfHeaderField({self.bvalue})'
    
