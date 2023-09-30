from .instruction import Instruction, Field
from typing import Literal

class UType(Instruction):

    # CHECK
    opcodes = [
        '1110011',
        '0010111',
        '0110111',
    ]
    
    instructions = {
        '0010111': 'AIUPC',                
        '0110111': 'LUI',                
    }

    fields = [
        Field('opcode', 0, 7),
        Field('rd', 7, 5),
        Field('imm', 12, 20),
    ]

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        concat = self.get('imm')
        
        immediate = int(concat, 2), len(concat)
        immediate = int(concat, 2)
        
        target_register = int(self.get('rd'), 2)
        
        try:
            instruction = self.instructions[self.get('opcode')]
        except KeyError:
            raise ValueError(f"Unsupported U-Type instruction: {self.source}")

        return f"{instruction} x{target_register}, x{immediate}"

    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('imm')}{self.get('rd')}{self.get('opciode')}"
        value = int(rep, 2)
        return value.to_bytes(4, endianess)

    def mne(self):
        try:
            return self.instructions[self.get('opcode')]
        except KeyError:
            raise ValueError(f"Unsupported U-Type instruction: {self.source}")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()