from .instruction import Instruction, Field
from typing import Literal

class BType(Instruction):

    # CHECK
    opcodes = ['1100011']

    fields = [
        Field('opcode', 0, 7),
        Field('imm[11]', 7, 1),
        Field('imm[4:1]', 8, 4),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('rs2', 20, 5),
        Field('imm[10:5]', 25, 6),
        Field('imm[12]', 31, 1),
    ]
    
    funcs = {
        "1100011": {
            "000": "BEQ",
            "001": "BNE",
            "100": "BLT",
            "101": "BGE",
            "110": "BLTU",
            "111": "BGEU",
        },
    }

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self):
        concat = f"{self.get('imm[12]')}{self.get('imm[11]')}{self.get('imm[10:5]')}{self.get('imm[4:1]')}"
        
        immediate = int(concat, 2)
        
        source_register_1 = int(self.get('rs1'), 2)
        
        source_register_2 = int(self.get('rs2'), 2)
        
        try:
            instruction = self.funcs[self.get('opcode')][self.get('funct3')]
        except KeyError:
            raise ValueError("Unsupported instruction")

        return f"{instruction} x{source_register_1}, x{source_register_2}, {immediate}"

    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('imm[12]')}{self.get('imm[10:5]')}{self.get('rs2')}{self.get('rs1')}{self.get('funct3')}{self.get('imm[4:1]')}{self.get('imm[11]')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(4, endianess)
        
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()