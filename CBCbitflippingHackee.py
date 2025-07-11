from AESinECB import AES_128_ECB_decrypt, AES_128_ECB_encrypt
from HexString import HexString
from K_eq_v_transformer import K_eq_v_transformer
from rand_hex_string import rand_hex_string

class CBCbitflippingHackee:
    def __init__(self, prefix: str, suffix: str):
        self._prefix = prefix
        self._suffix = suffix
        self._key = rand_hex_string(16,16)
        self._transformer = K_eq_v_transformer(seperator=";", equal_sign="=")
    
    def prefix(self): return self._prefix
    def suffix(self): return self._suffix
    
    def _profile_code_from_userdata(self, userdata: str):
        if not self._transformer.accepts(userdata):
            raise ValueError("userdata contains illegal characters")
        
        return self._prefix + userdata + self._suffix
    
    def profile_for(self, userdata: str):
        code = self._profile_code_from_userdata(userdata)
        return AES_128_ECB_encrypt(HexString.from_raw_str(code), self._key)
    
    def decrypt_profile(self, ciphertext: HexString):
        code = AES_128_ECB_decrypt(ciphertext, self._key).to_raw_str()
        return self._transformer.decode(code)