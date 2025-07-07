import base64
from HexString import HexString
from EnglishString import EnglishString

class Base64String:

    def __init__(self, bytes: bytes):
        self.content = bytes
    
    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.decode('ascii')
    
    def __eq__(self, other: object):
        if not isinstance(other, Base64String):
            return NotImplemented
        return self.content == other.content

    @classmethod
    def from_hex(cls, hex: HexString):
        return Base64String(base64.b64encode(bytes(hex)))

    @classmethod
    def from_base64_str(cls, string: str):
        return cls(string.encode('ascii'))
    
    def to_english_string(self):
        return EnglishString(self.content.decode('ascii'))