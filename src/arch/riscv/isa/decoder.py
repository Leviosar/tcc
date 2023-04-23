from arch.common.isa.decoder import Decoder
from enums.riscv.isa import OpCode
from .instructions import Instruction, BType, IType, JType, RType, SType, UType, CType
from typing import List

class RiscVDecoder(Decoder):
    def decode(self, source: bytes):
        binary = bin(int.from_bytes(source, 'little'))

        types: List[Instruction] = [
            BType, IType, JType, RType, SType, UType
        ]

        opcode = binary[-7:]
        for type in types:
            if  opcode in type.opcodes:
                instruction = type(binary)

                return instruction
        else:
            raise ValueError("Unsupported instruction type")


        match opcode:
            case OpCode.AUIPC:
                pass
            case OpCode.LUI:
                pass
            case OpCode.JALR:
                pass
            case OpCode.JAL:
                pass
            case OpCode.B_TYPE:
                pass
            case OpCode.I_TYPE:
                rd = binary[20:25]
                funct3 = binary[17:20]
                rs1 = binary[12:17]
                imm = binary[0:12]
                pass
            case OpCode.S_TYPE:
                pass
            case OpCode.S_TYPE_F:
                pass
            case OpCode.U_TYPE:
                pass
            case OpCode.I_TYPE_A:
                pass
            case OpCode.I_TYPE_B:
                pass
            case OpCode.I_TYPE_F:
                pass
            case OpCode.I_TYPE_FEN:
                pass
            case OpCode.R4_TYPE_FMADD:
                pass
            case OpCode.R4_TYPE_FNMADD:
                pass
            case OpCode.R4_TYPE_FMSUB:
                pass
            case OpCode.R4_TYPE_FNMSUB:
                pass
            case OpCode.R_TYPE:
                rd = binary[20:25]
                funct3 = binary[17:20]
                rs1 = binary[12:17]
                rs2 = binary[7:12]
                funct7 = binary[0:7]
                pass
            case OpCode.R_TYPE_F:
                pass
            case OpCode.R_TYPE_W:
                pass
            case OpCode.R_TYPE_AMO:
                pass
        print(binary[2:].zfill(32))
        return super().decode(source)