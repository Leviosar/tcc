from enum import Enum

class ABI(Enum):
    System_V = 0	
    HP_UX = 1	
    NetBSD = 2	
    Linux = 3	
    GNU_Hurd = 4	
    Solaris = 6	
    AIX_Monterey = 7	
    IRIX = 8	
    FreeBSD = 9	
    Tru64 = 10	
    Novell_Modesto = 11	
    OpenBSD = 12
    OpenVMS = 13
    NonStop_Kernel = 14
    AROS = 15
    FenixOS = 16
    Nuxi_CloudABI = 17
    Stratus_Technologies_OpenVOS = 18
    
class BitFormat(Enum):
    INVALID = 0
    BIT_32 = 1
    BIT_64 = 2

class Endianess(Enum):
    INVALID = 0
    LSB = 1
    MSB = 2
    
class ElfType(Enum):
    NONE = 0 # Unknown.
    RELO = 1 # Relocatable file.
    EXEC = 2 # Executable file.
    DYNA = 3 # Shared object.
    CORE = 4 # Core file.
    
class MachineType(Enum):
    NONE = 0
    X86 = 3
    MIPS = 8
    PC_32 = 20
    PC_64 = 21
    ARM_32 = 40
    IA64 = 50
    AMD_X86 = 62
    ARM_64 = 183
    RISCV = 243
    
class ProgramType(Enum):
    NULL = 0	# Program header table entry unused.
    LOAD = 1	# Loadable segment.
    DYNAMIC = 2 # Dynamic linking information.
    INTERP = 3  # Interpreter information.
    NOTE = 4	# Auxiliary information.
    SHLIB = 5   # Reserved.
    PHDR = 6	# Segment containing program header table itself.
    TLS = 7     # Thread-Local Storage template.
    
# Source: https://refspecs.linuxbase.org/elf/gabi4+/ch5.pheader.html#p_flags
class ProgramFlags(Enum):
    X   = 1
    W   = 2
    R   = 4
    WX  = 3
    RX  = 5
    RW  = 6
    RWX = 7