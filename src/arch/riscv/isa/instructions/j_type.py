from .instruction import Instruction, Field
from utils.binary_manipulation import twos_comp


class JType(Instruction):

    # CHECK
    opcodes = ['1100111', '1101111']

    fields = [
        Field('opcode', 0, 7),
        Field('rd', 7, 5),
        Field('imm[19:12]', 12, 8),
        Field('imm[11]', 20, 1),
        Field('imm[10:1]', 21, 10),
        Field('imm[20]', 31, 1),
    ]

    def __init__(self, source: str):
        super().__init__(source)

    def asm(self):
        instructions = {
            '1101111': 'jal',
            '1100111': 'j',
            'j': '1100111'
        }

        # J instructions have immediates with a hardcoded 0 on LSB
        concat =  self.get('imm[20]') + self.get('imm[19:12]') + self.get('imm[11]') + self.get('imm[10:1]') + '0'
        
        immediate = twos_comp(int(concat, 2), len(concat))
        
        register = int(self.get('rd'), 2)

        instruction = instructions[self.get('opcode')] 

        return f"{instruction} x{register}, {immediate}"

    def __repr__(self):
        return self.asm()