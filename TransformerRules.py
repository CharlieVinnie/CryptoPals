from typing import Callable


class DoesNot:
    
    @classmethod
    def include(cls, bans: str) -> Callable[[str],bool]:
        return lambda s: all(b not in s for b in bans)