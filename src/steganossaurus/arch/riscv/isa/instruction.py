from steganossaurus.arch.riscv.isa.decoder import RiscVDecoder


class Instruction:
    code: bytes
    _decoder: RiscVDecoder

    def __init__(self, code: bytes):
        self.code = code
        self._decoder = RiscVDecoder()

    def decode(self) -> str:
        return self._decoder.decode(self.code)
