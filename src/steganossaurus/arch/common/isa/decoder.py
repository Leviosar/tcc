import abc


class Decoder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def decode(self, source: bytes) -> str:
        return
