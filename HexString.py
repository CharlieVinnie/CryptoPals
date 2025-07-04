from __future__ import annotations

class HexString:

    def __init__(self, bytes: bytes):
        self.content = bytes

    @classmethod
    def from_str(cls, string: str):
        return cls(bytes.fromhex(string))

    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.hex()
    
    def __xor__(self, other: HexString):
        if len(self.content) != len(other.content):
            raise ValueError("Different Lengths when xoring HexString")
        return HexString(bytes(x^y for (x,y) in zip(self.content, other.content)))
