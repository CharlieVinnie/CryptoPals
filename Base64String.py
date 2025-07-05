import base64
from HexString import HexString

class Base64String:

    def __init__(self, string: str):
        self.content = string.encode('ascii')
    
    def __bytes__(self):
        return self.content
    
    def __str__(self):
        return self.content.decode('ascii')

    @classmethod
    def from_hex(cls, hex: HexString):
        return Base64String(base64.b64encode(bytes(hex)).decode('ascii'))

