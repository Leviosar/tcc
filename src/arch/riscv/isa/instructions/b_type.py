from .instruction import Instruction, Field

class BType(Instruction):

    # CHECK
    opcodes = ['1100011']

    fields = [
        Field('imm[11]', 7, 1),
        Field('imm[4:1]', 8, 4),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('rs2', 20, 5),
        Field('imm[10:5]', 25, 6),
        Field('imm[12]', 31, 1),
    ]

    def __init__(self, source: str):
        super().__init__(source)