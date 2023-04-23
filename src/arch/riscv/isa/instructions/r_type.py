from .instruction import Instruction, Field

class RType(Instruction):

    opcodes = ['0110011']

    fields = [
        Field('rd', 7, 5),
        Field('funct3', 12, 3),
        Field('rs1', 15, 5),
        Field('rs2', 20, 5),
        Field('funct7', 25, 7),
    ]

    def __init__(self, source: str):
        super().__init__(source)