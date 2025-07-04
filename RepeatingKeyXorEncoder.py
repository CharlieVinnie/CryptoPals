from XorEncoder import XorEncoder
from HexString import HexString
import itertools

class RepeatingKeyXorEncoder(XorEncoder):
    @classmethod
    def get_mask(cls, key: HexString, length: int):
        generator = itertools.islice(itertools.cycle(bytes(key)), length)
        return HexString(bytes(generator))
