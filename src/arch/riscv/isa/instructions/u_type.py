from .instruction import Instruction, Field

class UType(Instruction):

    # CHECK
    opcodes = ['1110011']

    fields = [
        Field('rd', 7, 5),
        Field('imm', 12, 20),
    ]

    def __init__(self, source: str):
        super().__init__(source)