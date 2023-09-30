from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal

class CAType(Instruction):

    opcodes = ['01']

    fields = [
        Field('opcode', 0, 2),
        Field("rs2", 2, 3),
        Field('funct2', 5, 2),
        Field("rd/rs1", 7, 3),
        Field('funct6', 10, 6),
    ]
    
    functs = {
        # RV32
        "100011": {
            "00": "C.SUB",
            "01": "C.XOR",
            "10": "C.OR",
            "11": "C.AND",
        },
        "100111": {
            "00": "C.SUBW",
            "01": "C.ADDW",
        },
    }
    """
        Table of instructions indexed by [funct6][funct2] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        target_register = int(self.get("rd/rs1"), 2)
        
        source_register_2 = int(self.get("rs2"), 2)
        
        try:
            instruction = self.functs[self.get('funct6')][self.get('funct2')]
        except KeyError:
            raise ValueError(f"Unsupported CA-Type instruction: {self.source}")

        return f"{instruction} x{target_register}, x{source_register_2}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('funct6')}{self.get('rd/rs1')}{self.get('funct2')}{self.get('rs2')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(2, endianess)
    
    def mne(self):
        try:
            return self.functs[self.get('opcode')]
        except KeyError:
            raise ValueError(f"Unsupported CA-Type instruction: {self.source}")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()