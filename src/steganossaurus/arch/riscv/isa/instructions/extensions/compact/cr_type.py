from steganossaurus.arch.riscv.isa.instructions.instruction import Instruction, Field
from typing import Literal


class CRType(Instruction):
    opcodes = ["10"]

    fields = [
        Field("opcode", 0, 2),
        Field("rs2", 2, 5),
        Field("rd/rs1", 7, 5),
        Field("funct4", 12, 4),
    ]

    functs = {
        "10": {
            "1000": [
                # The difference between C.JR and C.MV is the rs2 value
                {
                    "mne": "C.JR",
                    "condition": lambda rs2: rs2 == "00000",
                },
                {
                    "mne": "C.MV",
                    "condition": lambda rs2: rs2 != "00000",
                },
            ],
            "1001": [
                # The difference between C.JALR and C.ADD is the rs2 value
                {
                    "mne": "C.JALR",
                    "condition": lambda rs2: rs2 == "00000",
                },
                {
                    "mne": "C.ADD",
                    "condition": lambda rs2: rs2 != "00000",
                },
            ],
        }
    }
    """
        Table of instructions indexed by [opcode][funct4] fields.
    """

    def __init__(self, source: str):
        super().__init__(source)

    def asm(self) -> str:
        target_register = int(self.get("rd/rs1"), 2)

        source_register_2 = int(self.get("rs2"), 2)

        try:
            candidates = self.functs[self.get("opcode")][self.get("funct4")]
            instruction = next(
                filter(lambda i: i["condition"](self.get("rs2")), candidates)
            )["mne"]
        except KeyError:
            raise ValueError(f"Unsupported CR-Type instruction: {self.source}")

        return f"{instruction} x{target_register}, x{source_register_2}"

    def bin(self, endianess: Literal["little", "big"] = "little") -> bytes:
        rep = f"{self.get('funct4')}{self.get('rd/rs1')}{self.get('rs2')}{self.get('opcode')}"
        value = int(rep, 2)
        return value.to_bytes(2, endianess)

    def mne(self):
        try:
            candidates = self.functs[self.get("opcode")][self.get("funct4")]
            return next(filter(lambda i: i["condition"](self.get("rs2")), candidates))[
                "mne"
            ]
        except KeyError:
            raise ValueError(f"Unsupported CR-Type instruction: {self.source}")

    def __repr__(self):
        return self.asm()

    def __str__(self):
        return self.asm()
