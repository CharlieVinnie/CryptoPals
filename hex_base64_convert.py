from __future__ import annotations
import base64

class HexString:

    def __init__(self, bytes: bytes):
        self.content = bytes

    def to_bytes(self):
        return self.content
    
    def to_string(self):
        return self.content.hex()
    
    def __xor__(self, other: HexString):
        if len(self.content) != len(other.content):
            raise ValueError("Different Lengths when xoring HexString")
        return HexString(bytes(x^y for (x,y) in zip(self.content, other.content)))

class Base64String:

    def __init__(self, bytes: bytes):
        self.content = bytes
    
    def to_bytes(self):
        return self.content
    
    def to_string(self):
        return self.content.decode('ascii')


def str_to_HexString(string: str):
    return HexString(bytes.fromhex(string))

def hex_to_base64(hex_string: HexString):
    return Base64String(base64.b64encode(hex_string.to_bytes()))
