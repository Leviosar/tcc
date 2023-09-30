from steganossaurus.arch.common.isa.decoder import Decoder
from .instructions import Instruction, BType, IType, JType, RType, SType, UType, CType
from .instructions.extensions.compact import CRType, CAType, CIType, CJType, CBType
from typing import Optional, Tuple
from io import BufferedRandom

class RiscVDecoder(Decoder):
    def decode(self, pointer: BufferedRandom) -> Tuple[Optional[Instruction], int]:
        # Checking for 2-byte compact instruction
        source = pointer.read(2)
        binary = bin(int.from_bytes(source, 'little'))
        
        opcode_hint = binary[-2:]
        
        if opcode_hint != "11":
            types = [
                CRType, CAType, CIType, CJType, CBType
            ]

            opcode = binary[-2:]
            opcode = opcode.replace("0b", "")
            opcode = opcode.rjust(2, "0")
            
            for type in types:
                if opcode in type.opcodes:
                    try:
                        instruction = type(binary)
                        instruction.asm()
                        return (instruction, 2)
                    except ValueError as e:
                        pass
            else:
                raise ValueError(f"Unsupported compact instruction type: {binary} with opcde {opcode}")
        else:
            # Return 2 bytes to look for a 4-byte normal instruction
            pointer.seek(pointer.tell() - 2)
            
            source = pointer.read(4)
            binary = bin(int.from_bytes(source, 'little'))
            
            types = [
                BType, IType, JType, RType, SType, UType, CType
            ]

            opcode = binary[-7:]
            opcode = opcode.replace("0b", "")
            opcode = opcode.rjust(7, "0")
            
            for type in types:
                if opcode in type.opcodes:
                    try:
                        instruction = type(binary)
                        return (instruction, 4)
                    except ValueError as e:
                        print(f"Unsupported instruction type: {binary} with opcde {opcode}")    
            else:
                raise ValueError(f"Unsupported instruction type: {binary} with opcde {opcode}")