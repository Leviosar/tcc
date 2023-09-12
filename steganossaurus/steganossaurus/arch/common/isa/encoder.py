import abc

class Encoder(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def encode(self, source: str) -> bytes:
        return 