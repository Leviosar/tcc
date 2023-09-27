from .instruction import Instruction, Field

class SType(Instruction):

    # CHECK
    opcodes = ['0100011']

    fields = [
        Field('imm1', 7, 5),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('rs2', 20, 5),
        Field('imm2', 25, 7),
    ]

    def __init__(self, source: str):
        super().__init__(source)