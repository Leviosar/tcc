from io import BufferedRandom
import pdb


class StringTable:
    content: bytes

    def __init__(self, pointer: BufferedRandom, start: int, size: int) -> None:
        pointer.seek(start)
        self.content = pointer.read(size)

    def get(self, start):
        haystack = self.content[start:]

        for i, char in enumerate(haystack):
            if char == 0:
                return haystack[:i]
