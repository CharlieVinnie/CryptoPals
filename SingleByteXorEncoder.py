from XorEncoder import XorEncoder
from HexString import HexString

class SingleByteXorEncoder(XorEncoder):
    
    @classmethod
    def get_mask(cls, key: HexString, length: int):
        if len(key) != 1:
            raise ValueError("key must be a single byte")
        return HexString(bytes(key) * length)
    