from abc import ABC, abstractmethod
from HexString import HexString

class HexEncoder(ABC):
    @classmethod
    @abstractmethod
    def encode(cls, input: HexString, key: HexString) -> HexString: pass