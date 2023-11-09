import os
import pathlib
from tabulate import tabulate
from steganossaurus.elf.parser import parse
from steganossaurus.utils.logger import setup_logger
from steganossaurus.utils.crypto import encrypt
from typing import Literal, Union
from fractions import Fraction

import logging

def profile(file: str, log_level: Literal["debug", "info", "warning", "error", "critical"], message: Union[str, None] = None):
    setup_logger(log_level)
    
    capacity: int = 0
    instruction_generator = parse(file, ["ADD", "AND", "OR", "BEQ", "BNE"])
    natural_bits = [0, 0]

    for decoded_instruction, address, pointer in instruction_generator:
        rs1 = decoded_instruction.get("rs1")
        rs2 = decoded_instruction.get("rs2")

        # Can't encode if the registers are the same
        if rs1 == rs2:
            continue
        elif rs1 > rs2:
            natural_bits[1] += 1
        else:
            natural_bits[0] += 1
            
        capacity += 1

    logging.info(f"File size (in Bytes): {os.path.getsize(file)}")
    logging.info(f"Encoding capacity (in Bytes): {(capacity // 8) - 1}")
    logging.info(f"KB per bit: {((os.path.getsize(file) / 1024) // capacity)}")

    if message is not None:
        # Password here doesn't matter, the message is only used for profiling
        encrypted_message = encrypt(message.encode("ascii"), "big_bad_wolf")

        # Splits message into ascii codepoints list
        encrypted_message = list(encrypted_message)

        print(f"Message size (encrypted, in Bytes): {len(encrypted_message) + 1}")

    return (
        os.path.getsize(file) * 8,
        capacity,
        Fraction(capacity, os.path.getsize(file) * 8),
        (natural_bits[0], natural_bits[1])
    )

def absoluteFilePaths(directory):
    files = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            # files.append(os.path.abspath(pathlib.Path(os.path.join(dirpath, f))))
            files.append(f"./steganossaurus/bin/pg/{f}")
    return files
            
filenames = absoluteFilePaths("F:\\Dev\\ufsc\\tcc\\src\\steganossaurus\\bin\\pg")
filenames.append("./steganossaurus/bin/vmlinux")
filenames.append("./steganossaurus/bin/hello")
results = []
headers = ["name", "filesize", "capacity", "proportion"]

for filename in filenames:
    data = profile(filename, "info", "FLA")
    print(f"{filename} & {(data[1]/data[0] * 100):.2f}\\% \\\\")
    results.append([filename, data[0], data[1], f"{(data[1]/data[0] * 100):.2f} %"])

    
print(tabulate(results, headers))

avg = sum(map(lambda i: (i[2]/i[1] * 100), results)) / len(results)

print(f"Média de encoding rate: {avg:.2f}%")