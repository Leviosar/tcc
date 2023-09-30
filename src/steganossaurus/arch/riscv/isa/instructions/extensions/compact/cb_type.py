from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal

class CBType(Instruction):

    opcodes = ["01"]

    fields = [
        Field("opcode", 0, 2),
        Field("imm[5]", 2, 1),
        Field("imm[2:1]", 3, 2),
        Field("imm[7:6]", 5, 2),
        Field("rd/rs1", 7, 3),
        Field("imm[4:3]", 10, 2),
        Field("imm[8]", 12, 1),
        Field("funct3", 13, 3),
    ]
    
    functs = {
        "110": "C.BEQZ",
        "101": "C.BNEZ",
    }
    """
        Table of instructions indexed by [funct3] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        target_register = int(self.get("rd/rs1"), 2)
        
        try:
            instruction = self.functs[self.get("funct3")]
        except KeyError:
            raise ValueError(f"Unsupported CI-Type instruction: {self.source}")
        
        imm_fields = [
            "imm[2:1]",
            "imm[4:3]",
            "imm[5]",
            "imm[7:6]",
            "imm[8]",
        ]
        
        concat = ""
        for field in imm_fields:
            concat += self.get(field)
            
        immediate = int(concat, 2)

        return f"{instruction} x{target_register}, {immediate}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:        
        rep = f"{self.get('funct3')}{self.get('imm[8]')}{self.get('imm[4:3]')}{self.get('rd/rs1')}{self.get('imm[7:6]')}{self.get('imm[2:1]')}{self.get('imm[5]')}{self.get('opcode')}"
                 
        value = int(rep, 2)
        return value.to_bytes(2, endianess)
    
    def mne(self):
        try:
            return self.functs[self.get("funct3")]
        except KeyError:
            raise ValueError(f"Unsupported CB-Type instruction: {self.source}")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()