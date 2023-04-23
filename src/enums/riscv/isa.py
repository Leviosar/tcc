from enum import Enum


class OpCode(Enum):
    AUIPC = "0010111"
    LUI = "0110111"
    JALR = "1100111"
    JAL = "1101111"
    B_TYPE = "1100011"
    I_TYPE = "0000011"
    S_TYPE = "0100011"
    S_TYPE_F = "0100111"
    U_TYPE = "1110011"
    I_TYPE_A = "0010011"
    I_TYPE_B = "0011011"
    I_TYPE_F = "0000111"
    I_TYPE_FEN = "0001111"
    R4_TYPE_FMADD = "1000011"
    R4_TYPE_FNMADD = "1001111"
    R4_TYPE_FMSUB = "1000111"
    R4_TYPE_FNMSUB = "1001011"
    R_TYPE = "0110011"
    R_TYPE_F = "1010011"
    R_TYPE_W = "0111011"
    R_TYPE_AMO = "0101111"

class BTypeFunction(Enum):
    BEQ = "000"
    BNE = "001"
    BLT = "100"
    BGE = "101"
    BLTU = "110"
    BGEU = "111"

class ITypeFunction(Enum):
    LB = "000"
    LH = "001"
    LW = "010"
    LBU = "100"
    LHU = "101"
    LWU = "110"
    LD = "011"

class ITypeAFunction(Enum):
    ADDI = "000"
    SLTI = "010"
    SLTIU = "011"
    XORI = "100"
    ORI = "110"
    ANDI = "111"
    SLLI = "001"
    ITypeA = "101"
