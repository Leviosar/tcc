from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Field:
    name: str
    start: int
    size: int
    value: Optional[str] = None

class Instruction:
    opcodes: List[str]

    fields: List[Field]

    def get(self, needle):
        return next(filter(lambda field: field.name == needle, self.fields)).value

    def __init__(self, source: str):
        reverse = source[::-1]
        reverse = reverse.replace('b0', '')
        print('fonte')
        print(reverse)
        print('campos')
        for field in self.fields:
            # bin(int.from_bytes(source, 'little'))
            print(field.name)
            field.value = reverse[field.start : field.start + field.size][::-1]
            print(field.value)
