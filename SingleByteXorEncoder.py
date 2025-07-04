from HexEncoder import HexEncoder
from HexString import HexString

class SingleByteXorEncoder(HexEncoder):
    
    @classmethod
    def get_mask(cls, key: HexString, length: int):
        if len(key) != 1:
            raise ValueError("key must be a single byte")
        return bytes(key) * length
    