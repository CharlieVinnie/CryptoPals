from HexString import HexString
from typing import Callable


class DoesNot:
    
    @classmethod
    def include(cls, bans: str) -> Callable[[HexString],bool]:
        return lambda s: all(ord(b) not in s for b in bans)