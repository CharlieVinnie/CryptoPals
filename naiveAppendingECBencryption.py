from HexString import HexString
from AESinECB import AES_128_ECB_encrypt
from rand_hex_string import rand_hex_string
from Encryption import Encryption

class NaiveAppendingECBencryption(Encryption):
    
    def __init__(self, secret: HexString, key: HexString):
        self.secret = secret
        self.key = key
    
    def encrypt(self, input: HexString):
        input = input + self.secret
        return AES_128_ECB_encrypt(input,self.key)
    
    @classmethod
    def create(cls, secret: HexString):
        return cls(secret, rand_hex_string(16,16))