from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal

class CJType(Instruction):

    opcodes = ['01']

    fields = [
        Field('opcode', 0, 2),
        Field('imm[5]', 2, 1),
        Field('imm[3:1]', 3, 3),
        Field('imm[7]', 6, 1),
        Field('imm[6]', 7, 1),
        Field('imm[10]', 8, 1),
        Field('imm[9:8]', 9, 2),
        Field('imm[4]', 11, 1),
        Field('imm[11]', 12, 1),
        Field('funct3', 13, 3),
    ]
    
    functs = {
        # RV32
        "101": "C.J",
        "001": "C.JAL",
    }
    """
        Table of instructions indexed by [funct3] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        concat = ""
        
        imm_fields = [
            'imm[3:1]',
            'imm[4]',
            'imm[5]',
            'imm[6]',
            'imm[7]',
            'imm[9:8]',
            'imm[10]',
            'imm[11]',
        ]
        for field in imm_fields:
            concat += self.get(field)
        
        try:
            instruction = self.functs[self.get('funct3')]
        except KeyError:
            raise ValueError(f"Unsupported CJ-Type instruction: {self.source}")

        immediate = int(concat, 2)
        
        return f"{instruction} x{immediate}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        imm_fields = [
            'imm[5]',
            'imm[3:1]',
            'imm[7]',
            'imm[6]',
            'imm[10]',
            'imm[9:8]',
            'imm[4]',
            'imm[11]',
        ]
        
        concat = ""
        for field in imm_fields:
            concat += self.get(field)
            
        rep = f"{self.get('funct3')}{concat}{self.get('opcode')}"
        
        value = int(rep, 2)
        return value.to_bytes(2, endianess)
    
    def mne(self):
        try:
            return self.functs[self.get('funct3')]
        except KeyError:
            raise ValueError(f"Unsupported CJ-Type instruction: {self.source}")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()