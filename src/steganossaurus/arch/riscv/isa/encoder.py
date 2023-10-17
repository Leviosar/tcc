from steganossaurus.arch.common.isa.encoder import Encoder
from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction


class RiscVEncoder(Encoder):
    def encode(self, source: Instruction) -> bytes:
        return source.bin()
