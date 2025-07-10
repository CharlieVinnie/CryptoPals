from HexString import HexString
from rand_hex_string import rand_hex_string
from Profile import ProfileCreator
from K_eq_v_transformer import K_eq_v_transformer
from AESinECB import AES_128_ECB_encrypt, AES_128_ECB_decrypt

from random import randint

class ECBkeqvHackee:
    def __init__(self):
        self._key = rand_hex_string(16,16)
        self._profile_creator = ProfileCreator(
            {"uid": lambda: str(randint(0,100)),
             "role": lambda: "user"},
            {"email"}
        )
        self._transformer = K_eq_v_transformer(seperator="&", equal_sign="=")

    def _encode_profile_with_email(self, email: str):
        if not self._transformer.accepts(email):
            raise ValueError("email contains illegal characters")
        
        profile = self._profile_creator.create({"email": email})
        return self._transformer.encode(profile)

    def profile_for(self, email: str):
        code = self._encode_profile_with_email(email)
        return AES_128_ECB_encrypt(HexString.from_raw_str(code), self._key)
    
    def decrypt_profile(self, ciphertext: HexString):
        code = AES_128_ECB_decrypt(ciphertext, self._key)
        return self._transformer.decode(code.to_raw_str())