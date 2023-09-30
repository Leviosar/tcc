from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal

class CSType(Instruction):

    opcodes = ['01']

    fields = [
        Field('opcode', 0, 2),
        Field('rs2', 2, 5),
        Field('rd/rs1', 7, 5),
        Field('funct4', 12, 4),
    ]
    
    functs = {
        # RV32
        "1001": "C.ADD",
        "1000": "C.MV",
    }
    """
        Table of instructions indexed by [funct4] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        target_register = int(self.get('rd/rs1'), 2)
        
        source_register_2 = int(self.get('rs2'), 2)
        
        try:
            instruction = self.functs[self.get('funct4')]
        except KeyError:
            raise ValueError("Unsupported instruction")

        return f"{instruction} x{target_register}, x{source_register_2}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('funct4')}{self.get('rd/rs1')}{self.get('rs2')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(2, endianess)
    
    def mne(self):
        try:
            return self.functs[self.get('opcode')]
        except KeyError:
            raise ValueError("Unsupported instruction")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()