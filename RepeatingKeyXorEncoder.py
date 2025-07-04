from XorEncoder import XorEncoder
from HexString import HexString
from typing import Iterator
import itertools

class RepeatingKeyXorEncoder(XorEncoder):
    @classmethod
    def get_mask(cls, key: HexString, length: int):
        def generator() -> Iterator[int]:
            yield from itertools.cycle(bytes(key))
        return HexString(bytes(generator())[:length])
