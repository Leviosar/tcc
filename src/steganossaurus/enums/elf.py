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
    
class SectionType(Enum):
    NULL = 0	        # Program header table entry unused.
    PROGBITS = 1	    # Program data.
    SYMTAB = 2          # Symbol table.
    STRTAB = 3          # String table
    RELA = 4	        # Relocation entries with addends
    HASH = 5            # Symbol hash table.
    DYNAMIC = 6	        # Dynamic linking information
    NOTE = 7            # Notes.
    NOBITS = 8          # Program space with no data (bss)
    REL = 9             # Relocation entries, no addends
    SHLIB = 10          # Reserved
    DYNSYM = 11         # Dynamic linker symbol table
    INIT_ARRAY = 12     # Array of constructors
    FINI_ARRAY = 13     # Array of destructors
    PREINIT_ARRAY = 14  # Array of pre-constructors
    GROUP = 15          # Section group
    SYMTAB_SHNDX = 16   # Extended section indices
    NUM = 17            # Number of defined types.

    @classmethod
    def _list(cls):
        return [
            cls.NULL,
            cls.PROGBITS,
            cls.SYMTAB,
            cls.STRTAB,
            cls.RELA,
            cls.HASH,
            cls.DYNAMIC,
            cls.NOTE,
            cls.NOBITS,
            cls.REL,
            cls.SHLIB,
            cls.DYNSYM,
            cls.INIT_ARRAY,
            cls.FINI_ARRAY,
            cls.PREINIT_ARRAY,
            cls.GROUP,
            cls.SYMTAB_SHNDX,
            cls.NUM,
        ]

    @classmethod
    def from_int(cls, n: int):
        return cls._list()[n]
    
# Source: https://refspecs.linuxbase.org/elf/gabi4+/ch5.pheader.html#p_flags
class ProgramFlags(Enum):
    X   = 1
    W   = 2
    R   = 4
    WX  = 3
    RX  = 5
    RW  = 6
    RWX = 7