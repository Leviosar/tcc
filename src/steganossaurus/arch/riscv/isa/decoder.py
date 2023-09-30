from steganossaurus.arch.common.isa.decoder import Decoder
from steganossaurus.enums.riscv.isa import OpCode
from .instructions import Instruction, BType, IType, JType, RType, SType, UType, CType
from typing import Optional, Tuple
from io import BufferedRandom

class RiscVDecoder(Decoder):
    def decode(self, pointer: BufferedRandom) -> Tuple[Optional[Instruction], int]:
        # Checking for 2-byte compact instruction
        source = pointer.read(2)
        binary = bin(int.from_bytes(source, 'little'))
        
        opcode_hint = binary[-2:]
        
        if opcode_hint != "11":
            return (None, 2)
        else:
            # Return 2 bytes to look for a 4-byte normal instruction
            pointer.seek(pointer.tell() - 2)
            
            source = pointer.read(2)
            binary = bin(int.from_bytes(source, 'little'))
            
            types = [
                BType, IType, JType, RType, SType, UType, CType
            ]

            opcode = binary[-7:]
            opcode = opcode.replace("0b", "")
            opcode = opcode.rjust(7, "0")
            
            for type in types:
                if opcode in type.opcodes:
                    instruction = type(binary)

                    return (instruction, 4)
            else:
                raise ValueError(f"Unsupported instruction type: {binary} with opcde {opcode}")