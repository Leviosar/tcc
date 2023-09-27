from typing import List, Optional, Literal
from dataclasses import dataclass

@dataclass
class Field:
    name: str
    start: int
    size: int
    value: Optional[str] = None

class Instruction:
    opcodes: List[str]

    source: str
    
    fields: List[Field]


    def bin(self, endianess: Literal["little", "big"] = "little"):
        return int(0).to_bytes(4, endianess)
    

    def mne(self) -> str:
        return ""
    
    
    def get(self, needle):
        try: 
            return next(filter(lambda field: field.name == needle, self.fields)).value
        except StopIteration:
            raise KeyError(needle, self.fields)
    
    
    def set(self, needle: str, value: str):
        if (value == ''):
            value = '0'
                
        try: 
            field = next(filter(lambda field: field.name == needle, self.fields)) 
        except StopIteration:
            raise KeyError(needle, self.fields)
            
        if field.value is None:
            field.value = '0'
            
        field.value = value.rjust(field.size, '0')
        
        return value


    def __init__(self, source: str):
        self.source = source
        
        reverse = source[::-1]
        reverse = reverse.replace('b0', '')
        # print('fonte')
        # print(reverse)
        # print('campos')
        for field in self.fields:
            # bin(int.from_bytes(source, 'little'))
            # print(field.name)
            field.value = reverse[field.start : field.start + field.size][::-1]
            
            if (field.value == ''):
                field.value = '0'
            
            field.value = field.value.rjust(field.size, "0")
            # print(field.value)
