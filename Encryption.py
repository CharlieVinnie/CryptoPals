from abc import ABC, abstractmethod
from HexString import HexString

class Encryption(ABC):
    @abstractmethod
    def encrypt(self, input: HexString) -> HexString:
        pass