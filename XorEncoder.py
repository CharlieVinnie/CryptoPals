from abc import abstractmethod
from HexEncoder import HexEncoder
from HexString import HexString

class XorEncoder(HexEncoder):
    
    @classmethod
    @abstractmethod
    def get_mask(cls, key: HexString, length: int) -> HexString: pass
    
    @classmethod
    @abstractmethod
    def encode(cls, input: HexString, key: HexString):
        return input ^ cls.get_mask(key, len(input))