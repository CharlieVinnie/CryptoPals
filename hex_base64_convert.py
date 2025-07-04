import base64

class HexString:

    def __init__(self, string: str):
        self.content = bytes.fromhex(string)

    def to_bytes(self):
        return self.content

class Base64String:

    def __init__(self, bytes: bytes):
        self.content = bytes
    
    def to_bytes(self):
        return self.content
    
    def to_string(self):
        return self.content.decode('ANSI')

def hex_to_base64(hex_string: HexString):
    return Base64String(base64.b64encode(hex_string.to_bytes()))
