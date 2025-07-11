from AESinCBC import AES_128_CBC_decrypt, AES_128_CBC_encrypt
from HexString import HexString
from K_eq_v_transformer import K_eq_v_transformer
from rand_hex_string import rand_hex_string

class CBCbitflippingHackee:
    def __init__(self, prefix: HexString, suffix: HexString):
        self._prefix = prefix
        self._suffix = suffix
        self._key = rand_hex_string(16,16)
        self._iv = rand_hex_string(16,16)
        self._transformer = K_eq_v_transformer(seperator=";", equal_sign="=")
    
    def prefix(self): return self._prefix
    def suffix(self): return self._suffix
    
    def _profile_code_from_userdata(self, userdata: HexString):
        if not self._transformer.accepts(userdata):
            raise ValueError("userdata contains illegal characters")
        
        return self._prefix + userdata + self._suffix
    
    def profile_for(self, userdata: HexString):
        code = self._profile_code_from_userdata(userdata)
        return AES_128_CBC_encrypt(code, self._key, self._iv)
    
    def decrypt_profile(self, ciphertext: HexString):
        code = AES_128_CBC_decrypt(ciphertext, self._key, self._iv)
        return self._transformer.decode(code)