import base64
from HexString import HexString

class Base64String:

    def __init__(self, bytes: bytes):
        self.content = bytes
    
    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.decode('ascii')

    @classmethod
    def from_hex(cls, hex: HexString):
        return Base64String(base64.b64encode(bytes(hex)))

    @classmethod
    def from_base64_str(cls, string: str):
        return cls(base64.b64decode(string))