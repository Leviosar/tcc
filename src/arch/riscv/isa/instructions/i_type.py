from .instruction import Instruction, Field
from utils.binary_manipulation import twos_comp
from typing import Literal

class IType(Instruction):

    # CHECK
    opcodes = ['0010011', '0011011', '0000111', '0001111', '0000011']

    funcs = {
        # I-Type
        '0000011': {
            "000" : "LB",
            "001" : "LH",
            "010" : "LW",
            "100" : "LBU",
            "101" : "LHU",
            "110" : "LWU",
            "011" : "LD",
        },
        # I-Type-A
        '0010011': {
            "000" : "ADDI",
            "010" : "SLTI",
            "011" : "SLTIU",
            "100" : "XORI",
            "110" : "ORI",
            "111" : "ANDI",
            "001" : "SLLI",
            "101" : "I-type-a",
        },
        # I-Type-B
        '0011011': {
            "000" : "ADDIW",
            "001" : "SLLIW",
            "101" : "I-type-b",
        },
        # I-Type-F
        '0000111': {
            "011" : "FLD",
            "010" : "FLW",
        },
        # I-Type-fen
        '0001111': {
            "000" : "FENCE",
            "001" : "FENCE.I",
        },
    }

    fields = [
        Field('opcode', 0, 7),
        Field('rd', 7, 5),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('imm', 20, 12),
    ]

    def __init__(self, source: str):
        super().__init__(source)

    def asm(self):
        concat = self.get('imm')
        immediate = twos_comp(int(concat, 2), len(concat))
        immediate = int(concat, 2)
        
        target_register = int(self.get('rd'), 2)
        
        source_register = int(self.get('rs1'), 2)
        
        try:
            instruction = self.funcs[self.get('opcode')][self.get('funct3')]
        except KeyError:
            raise ValueError("Unsupported instruction")

        return f"{instruction} x{target_register}, x{source_register}, {immediate}"

    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('imm')}{self.get('rs1')}{self.get('funct3')}{self.get('rd')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(4, endianess)
        
    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()