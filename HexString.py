from __future__ import annotations
from EnglishString import EnglishString

class HexString:

    def __init__(self, bytes: bytes):
        self.content = bytes

    @classmethod
    def from_hex_str(cls, string: str):
        return cls(bytes.fromhex(string))
    
    @classmethod
    def from_raw_str(cls, string: str):
        return cls(string.encode('ascii'))

    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.hex()
    
    def __len__(self):
        return len(self.content)
    
    def __xor__(self, other: HexString):
        if len(self.content) != len(other.content):
            raise ValueError(f"Different Lengths when xoring HexString")
        return HexString(bytes(x^y for (x,y) in zip(self.content, other.content)))
    
    def to_english_string(self):
        return EnglishString(self.content.decode('ascii'))
