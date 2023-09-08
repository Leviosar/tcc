from arch.common.isa.encoder import Encoder
from arch.riscv.isa.instructions.instruction import Instruction

class RiscVEncoder(Encoder):
    def encode(self, source: Instruction) -> bytes: 
        return source.bin()