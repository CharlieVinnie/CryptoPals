from AESinECB import AES_128_ECB_encrypt
from HexString import HexString
from Encryption import Encryption
from rand_hex_string import rand_hex_string

class PreAppendingECBencryption(Encryption):
    
    def __init__(self, secret: HexString, key: HexString, prefix: HexString):
        self.secret = secret
        self.key = key
        self.prefix = prefix
    
    def encrypt(self, input: HexString):
        input = self.prefix + input + self.secret
        return AES_128_ECB_encrypt(input, self.key)
    
    @classmethod
    def create(cls, secret: HexString):
        return cls(secret, rand_hex_string(16,16), rand_hex_string(16,16))