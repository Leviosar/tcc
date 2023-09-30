from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal

class CIType(Instruction):

    opcodes = ["10"]

    fields = [
        Field("opcode", 0, 2),
        Field("imm[8:6]", 2, 3),
        Field("imm[7:6]", 2, 2),
        Field("imm[4:3]", 5, 2),
        Field("imm[4:2]", 4, 3),
        Field('rd/rs1', 7, 5),
        Field("imm[5]", 12, 1),
        Field("funct3", 13, 3),
    ]
    
    functs = {
        # RV32
        "001": {
            "mne": "C.FLDSP",     
            "imm": ["imm[4:3]", "imm[5]", "imm[8:6]"],
        },
        "101": {
            "mne": "C.LWSP",     
            "imm": ["imm[4:2]", "imm[5]", "imm[7:6]"],
        },
        "011": {
            "mne": "C.LDSP",
            "imm": ["imm[4:3]", "imm[5]", "imm[8:6]"],
        },
    }
    """
        Table of instructions indexed by [funct6][funct2] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        target_register = int(self.get("rd/rs1"), 2)
        
        try:
            instruction = self.functs[self.get("funct3")]["mne"]
        except KeyError:
            raise ValueError("Unsupported instruction")
        
        imm_fields = self.functs[self.get("funct3")]["imm"]
        
        concat = ""
        for field in imm_fields:
            concat += self.get(field)
        
        if "imm[4:2]" in imm_fields:
            concat = "00" + concat
        else:
            concat = "000" + concat
            
        immediate = int(concat, 2)

        return f"{instruction} x{target_register}, x{immediate}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        imm_fields = self.functs[self.get("funct3")]["imm"]
        
        if "imm[4:2]" in imm_fields:
            rep = f"{self.get('funct3')}{self.get('imm[5]')}{self.get('rd/rs1')}{self.get('imm[4:2]')}{self.get('imm[7:6]')}{self.get('opcode')}"
        else :
            rep = f"{self.get('funct3')}{self.get('imm[5]')}{self.get('rd/rs1')}{self.get('imm[4:3]')}{self.get('imm[8:6]')}{self.get('opcode')}"
                 
        value = int(rep, 2)
        return value.to_bytes(2, endianess)
    
    def mne(self):
        try:
            return self.functs[self.get("opcode")]
        except KeyError:
            raise ValueError("Unsupported instruction")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()