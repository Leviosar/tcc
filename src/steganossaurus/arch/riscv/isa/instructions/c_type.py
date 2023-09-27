from .instruction import Instruction, Field
from steganossaurus.utils.binary_manipulation import twos_comp

class CType(Instruction):
    """C (compact) extension for RV, 16 bit instructions used for code size optimization. All instructions from RV
    "default size" ISA have opcodes ending with '11', and the C extension uses 00, 01 and 10 opcode LSBs to determine
    a quadrant for the instruction

    Args:
        Instruction (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    # CHECK
    opcodes = ['00', '01', '10']
    
    quadrants = [
        
    ]

    # 'c.lwsp':   { isa: 'C',  xlens: 0b111, fmt: 'CI-type', funct3: '010', rdRs1Mask: 0b10, rdRs1Excl: [0], uimm: true, immBits: [[5], [[4,2],[7,6]]], opcode: C_OPCODE.C2 },
    # 'c.ldsp':   { isa: 'C',  xlens: 0b110, fmt: 'CI-type', funct3: '011', rdRs1Mask: 0b10, rdRs1Excl: [0], uimm: true, immBits: [[5], [[4,3],[8,6]]], opcode: C_OPCODE.C2 },
    # 'c.lqsp':   { isa: 'C',  xlens: 0b100, fmt: 'CI-type', funct3: '001', rdRs1Mask: 0b10, rdRs1Excl: [0], uimm: true, immBits: [[5], [4,[9,6]]],     opcode: C_OPCODE.C2 },
    # 'c.flwsp':  { isa: 'FC', xlens: 0b001, fmt: 'CI-type', funct3: '011', rdRs1Mask: 0b10,                 uimm: true, immBits: [[5], [[4,2],[7,6]]], opcode: C_OPCODE.C2 },
    # 'c.fldsp':  { isa: 'DC', xlens: 0b011, fmt: 'CI-type', funct3: '001', rdRs1Mask: 0b10,                 uimm: true, immBits: [[5], [[4,3],[8,6]]], opcode: C_OPCODE.C2 },

    # 'c.swsp':   { isa: 'C',  xlens: 0b111, fmt: 'CSS-type', funct3: '110', uimm: true, immBits: [[5,2],[7,6]], opcode: C_OPCODE.C2 },
    # 'c.sdsp':   { isa: 'C',  xlens: 0b110, fmt: 'CSS-type', funct3: '111', uimm: true, immBits: [[5,3],[8,6]], opcode: C_OPCODE.C2 },
    # 'c.sqsp':   { isa: 'C',  xlens: 0b100, fmt: 'CSS-type', funct3: '101', uimm: true, immBits: [[5,4],[9,6]], opcode: C_OPCODE.C2 },
    # 'c.fswsp':  { isa: 'FC', xlens: 0b001, fmt: 'CSS-type', funct3: '111', uimm: true, immBits: [[5,2],[7,6]], opcode: C_OPCODE.C2 },
    # 'c.fsdsp':  { isa: 'DC', xlens: 0b011, fmt: 'CSS-type', funct3: '101', uimm: true, immBits: [[5,3],[8,6]], opcode: C_OPCODE.C2 },


    # 'c.lw':     { isa: 'C',  xlens: 0b111, fmt: 'CL-type', funct3: '010', uimm: true, immBits: [[[5,3]],   [2,6]],   opcode: C_OPCODE.C0 },
    # 'c.ld':     { isa: 'C',  xlens: 0b110, fmt: 'CL-type', funct3: '011', uimm: true, immBits: [[[5,3]],   [[7,6]]], opcode: C_OPCODE.C0 },
    # 'c.lq':     { isa: 'C',  xlens: 0b100, fmt: 'CL-type', funct3: '001', uimm: true, immBits: [[[5,4],8], [[7,6]]], opcode: C_OPCODE.C0 },
    # 'c.flw':    { isa: 'FC', xlens: 0b001, fmt: 'CL-type', funct3: '011', uimm: true, immBits: [[[5,3]],   [2,6]],   opcode: C_OPCODE.C0 },
    # 'c.fld':    { isa: 'DC', xlens: 0b011, fmt: 'CL-type', funct3: '001', uimm: true, immBits: [[[5,3]],   [[7,6]]], opcode: C_OPCODE.C0 },

    # 'c.sw':     { isa: 'C',  xlens: 0b111, fmt: 'CS-type', funct3: '110', uimm: true, immBits: [[[5,3]],   [2,6]],   opcode: C_OPCODE.C0 },
    # 'c.sd':     { isa: 'C',  xlens: 0b110, fmt: 'CS-type', funct3: '111', uimm: true, immBits: [[[5,3]],   [[7,6]]], opcode: C_OPCODE.C0 },
    # 'c.sq':     { isa: 'C',  xlens: 0b100, fmt: 'CS-type', funct3: '101', uimm: true, immBits: [[[5,4],8], [[7,6]]], opcode: C_OPCODE.C0 },
    # 'c.fsw':    { isa: 'FC', xlens: 0b001, fmt: 'CS-type', funct3: '111', uimm: true, immBits: [[[5,3]],   [2,6]],   opcode: C_OPCODE.C0 },
    # 'c.fsd':    { isa: 'DC', xlens: 0b011, fmt: 'CS-type', funct3: '101', uimm: true, immBits: [[[5,3]],   [[7,6]]], opcode: C_OPCODE.C0 },

    funcs = {
        # C0
        '00': {
            '010': {
                'name': 'c.lw',
                'immBits': [[[5,3]], [2,6]]
            },
            '011': {
                'name': 'c.ld',
                'immBits': [[[5,3]],   [[7,6]]]
            },
            '001': {
                'name': 'c.lq',
                'immBits': [[[5,4],8], [[7,6]]]
            },
            # Floating point instructions below collide func field with integer instructions
            # '011': {
            #     'name': 'c.flw',
            #     'immBits': [[[5,3]],   [2,6]]
            # },
            # '001': {
            #     'name': 'c.fld',
            #     'immBits': [[[5,3]],   [[7,6]]]
            # },
            '110': {
                'name': 'c.sw',
                'immBits': [[[5,3]],   [2,6]],
            },
            '111': {
                'name': 'c.sd',
                'immBits': [[[5,3]],   [[7,6]]],
            },
            '101': {
                'name': 'c.sq',
                'immBits': [[[5,4],8], [[7,6]]]
            },
        },

        # C1

        # 'c.j':      { isa: 'C', xlens: 0b101, fmt: 'CJ-type', funct3: '101', immBits: [11,4,[9,8],10,6,7,[3,1],5], opcode: C_OPCODE.C1 },
        # 'c.jal':    { isa: 'C', xlens: 0b001, fmt: 'CJ-type', funct3: '001', immBits: [11,4,[9,8],10,6,7,[3,1],5], opcode: C_OPCODE.C1 },
        
        # 'c.beqz':   { isa: 'C', xlens: 0b111, fmt: 'CB-type', funct3: '110', immBits: [[8,[4,3]], [[7,6],[2,1],5]], opcode: C_OPCODE.C1 },
        # 'c.bnez':   { isa: 'C', xlens: 0b111, fmt: 'CB-type', funct3: '111', immBits: [[8,[4,3]], [[7,6],[2,1],5]], opcode: C_OPCODE.C1 },

        # 'c.li':       { isa: 'C', xlens: 0b111, fmt: 'CI-type', funct3: '010', rdRs1Mask: 0b10, rdRs1Excl: [0],                immBits: [[5],  [[4,0]]],   opcode: C_OPCODE.C1 },
        # 'c.lui':      { isa: 'C', xlens: 0b111, fmt: 'CI-type', funct3: '011', rdRs1Mask: 0b10, rdRs1Excl: [0,2], nzimm: true, immBits: [[17], [[16,12]]], opcode: C_OPCODE

        # 'c.addi':     { isa: 'C', xlens: 0b111, fmt: 'CI-type', funct3: '000', rdRs1Mask: 0b11, rdRs1Excl: [0], nzimm: true,             immBits: [[5], [[4,0]]],       opcode: C_OPCODE.C1 },
        # 'c.addiw':    { isa: 'C', xlens: 0b110, fmt: 'CI-type', funct3: '001', rdRs1Mask: 0b11, rdRs1Excl: [0],                          immBits: [[5], [[4,0]]],       opcode: C_OPCODE.C1 },
        # 'c.addi16sp': { isa: 'C', xlens: 0b111, fmt: 'CI-type', funct3: '011', rdRs1Mask: 0b00, rdRs1Val: 2,    nzimm: true,             immBits: [[9], [4,6,[8,7],5]], opcode: C_OPCODE.C1 },

        '01': {
            '101': {
                'name': 'c.j',
                'immBits': [11,4,[9,8],10,6,7,[3,1],5]
            },
            '001': {
                'name': 'c.jal',
                'immBits': [11,4,[9,8],10,6,7,[3,1],5]
            },
            '110': {
                'name': 'c.beqz',
                'immBits': [[8,[4,3]], [[7,6],[2,1],5]]
            },
            '111': {
                'name': 'c.bnez',
                'immBits': [[8,[4,3]], [[7,6],[2,1],5]]
            },
            '010': {
                'name': 'c.li',
                'immBits': [[5],  [[4,0]]]
            },
            '011': {
                'name': 'c.lui',
                'immBits': [[17], [[16,12]]]
            },
            '000': {
                'name': 'c.addi',
            },
            '001': {
                'name': 'c.addiw',
            },
            '011': {
                'name': 'c.addi16sp',
            },
        },
        # C2

        # 'c.jr':     { isa: 'C', xlens: 0b111, fmt: 'CR-type', funct4: '1000', rdRs1Mask: 0b01, rdRs1Excl: [0], rs2Val: 0, opcode: C_OPCODE.C2 },
        # 'c.jalr':   { isa: 'C', xlens: 0b111, fmt: 'CR-type', funct4: '1001', rdRs1Mask: 0b01, rdRs1Excl: [0], rs2Val: 0, opcode: C_OPCODE.C2 },

        '10': {
            '010': {
                'name': 'c.lwsp',
                'immBits': [[5], [[4,2],[7,6]]],
            },
            '011': {
                'name': 'c.ldsp',
                'immBits': [[5], [[4,3],[8,6]]],
            },
            '001': {
                'name': 'c.lqsp',
                'immBits': [[5], [4,[9,6]]],
            },
            '011': {
                'name': 'c.flwsp',
                'immBits': [[5], [[4,2],[7,6]]],
            },
            '001': {
                'name': 'c.fldsp',
                'immBits': [[5], [[4,3],[8,6]]]
            },
            '110': {
                'name': 'c.swsp',
                'immBits': [[5,2],[7,6]]
            },
            '111': {
                'name': 'c.fswsp',
                'immBits': [[5,2],[7,6]]
            },
            '101': {
                'name': 'c.fsdsp',
                'immBits': [[5,3],[8,6]]
            },
            '1000': {
                'name': 'c.jr',
            },
            '1001': {
                'name': 'c.jalr',
            },
        },
    }

    fields = [
        Field('opcode', 0, 2),
        Field('imm[4:0]', 2, 5),
        Field('rd/rs1', 7, 5),
        Field('imm[5]', 12, 1),
        Field('funct', 13, 3),
    ]

    def __init__(self, source: str):
        super().__init__(source)

    def asm(self):
        opcode = self.get('opcode')
        
        funct = self.get('funct')
        
        register = self.get('rd/rs1')
        
        if opcode == '01' and funct == '000' and register == '00000':
            return 'c.nop'
        
        concat =  self.get('imm')

        immediate = twos_comp(int(concat, 2), len(concat))
        
        target_register = int(self.get('rd'), 2)
        
        source_register = int(self.get('rs1'), 2)

        if (immediate == 0 and target_register == 0):
            return "c.nop"
        
        try:
            instruction = self.funcs[self.get('opcode')][self.get('funct3')]
        except KeyError:
            raise ValueError("Unsupported instruction")

        return f"{instruction} x{target_register}, x{source_register} {immediate}"

    def __repr__(self):
        return self.asm()