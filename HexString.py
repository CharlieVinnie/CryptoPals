from __future__ import annotations
from EnglishString import EnglishString
import base64
from typing import overload

class HexString:

    def __init__(self, bytes: bytes = b''):
        self.content = bytes

    @classmethod
    def from_hex_str(cls, string: str):
        return cls(bytes.fromhex(string))
    
    @classmethod
    def from_raw_str(cls, string: str):
        return cls(string.encode('ascii'))
    
    @classmethod
    def from_base64_str(cls, string: str):
        return cls(base64.b64decode(string))

    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.hex()
    
    def __len__(self):
        return len(self.content)
    
    @overload
    def __getitem__(self, index: slice) -> HexString: ...
    
    @overload
    def __getitem__(self, index: int) -> int: ...
    
    def __getitem__(self, index: slice | int):
        if isinstance(index, slice):
            return HexString(self.content[index])
        else:
            return self.content[index]
    
    def __add__(self, other: HexString):
        return HexString(self.content + other.content)
    
    def __mul__(self, times: int):
        return HexString(self.content * times)
    
    def __xor__(self, other: HexString):
        if len(self.content) != len(other.content):
            raise ValueError(f"Different Lengths when xoring HexString")
        return HexString(bytes(x^y for (x,y) in zip(self.content, other.content)))
    
    def __eq__(self, other: object):
        if not isinstance(other, HexString):
            return NotImplemented
        return self.content == other.content
    
    def to_english_string(self):
        return EnglishString(self.content.decode('ascii'))
