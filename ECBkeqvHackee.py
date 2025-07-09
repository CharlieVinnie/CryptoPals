from HexString import HexString
from rand_hex_string import rand_hex_string
from Profile import ProfileCreator
from K_eq_v_transformer import K_eq_v_transformer, DoesNot
from AESinECB import AES_128_ECB_encrypt, AES_128_ECB_decrypt

from random import randint

class ECBkeqvHackee:
    def __init__(self):
        self.key = rand_hex_string(16,16)
        self.profile_creator = ProfileCreator(
            {"uid": lambda: str(randint(0,100)),
             "role": lambda: "user"},
            {"email"}
        )
        self.transformer = K_eq_v_transformer(rules=[DoesNot.include("&=")])

    def _encode_profile_with_email(self, email: str):
        if not self.transformer.accepts(email):
            raise ValueError("email contains illegal characters")
        
        profile = self.profile_creator.create({"email": email})
        return self.transformer.encode(profile)

    def profile_for(self, email: str):
        code = self._encode_profile_with_email(email)
        return AES_128_ECB_encrypt(HexString.from_raw_str(code), self.key)
    
    def decrypt_profile(self, ciphertext: HexString):
        code = AES_128_ECB_decrypt(ciphertext, self.key)
        return self.transformer.decode(code.to_raw_str())