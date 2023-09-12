from .instruction import Instruction, Field
from typing import Literal

class RType(Instruction):

    opcodes = ['0110011', '0111011']

    fields = [
        Field('opcode', 0, 7),
        Field('rd', 7, 5),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('rs2', 20, 5),
        Field('funct7', 25, 7),
    ]
    
    funcs = {
        # RV32
        "0111011": {
            "0000000": {
                "000": "ADDW",
                "001": "SLLW",
                "101": "SRLW",
            },
            "0100000": {
                "000": "SUBW",
                "101": "SRAW",
            },
            "0000001": {
                "000": "MULW",
                "100": "DIVW",
                "101": "DIVUW",
                "110": "REMW",
                "111": "REMUW",
            },
        },
        # RV64
        "0110011": {
            "0000000": {
                "000": "ADD",
                "001": "SLI",
                "010": "SLT",
                "011": "SLTU",
                "100": "XOR",
                "101": "SLR",
                "110": "OR",
                "111": "AND",
            },
            "0100000": {
                "000": "SUB",
                "101": "SRA",
            },
            "0000001": {
                "000": "MUL",
                "001": "MULH",
                "010": "MULHSU",
                "011": "MULHU",
                "100": "DIV",
                "101": "DIVU",
                "110": "REM",
                "111": "REMU",
            }
        },
    }
    """
        Table of instructions indexed by [opcode][funct7][funct3] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)
        
    def asm(self) -> str:
        target_register = int(self.get('rd'), 2)
        
        source_register_1 = int(self.get('rs1'), 2)
        
        source_register_2 = int(self.get('rs2'), 2)
        
        try:
            instruction = self.funcs[self.get('opcode')][self.get('funct7')][self.get('funct3')]
        except KeyError:
            raise ValueError("Unsupported instruction")

        return f"{instruction} x{target_register}, x{source_register_1}, x{source_register_2}"
    
    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('funct7')}{self.get('rs2')}{self.get('rs1')}{self.get('funct3')}{self.get('rd')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(4, endianess)
    
    def mne(self):
        try:
            return self.funcs[self.get('opcode')][self.get('funct7')][self.get('funct3')]
        except KeyError:
            raise ValueError("Unsupported instruction")
    
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()