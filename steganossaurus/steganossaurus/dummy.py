from steganossaurus.arch.riscv.isa.instruction import Instruction
from steganossaurus.arch.riscv.isa.decoder import RiscVDecoder
import pdb

# try:
i = bytes(b"\x33\x85\x27\x00")
decoded_instruction = RiscVDecoder().decode(i)
# if (decoded_instruction.get('funct3') == '000' and decoded_instruction.opcodes[0] == '0010011'):
# if (str(decoded_instruction) == "ADDI x0, x0, 0"):
print(f"{decoded_instruction}")
# except ValueError:
#     i = bytes(b"\x13\x00\x00\x00")
#     print(f"Unsupported {bin(int.from_bytes(i, 'little'))}")
#     pass