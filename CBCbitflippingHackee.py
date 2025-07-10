from K_eq_v_transformer import K_eq_v_transformer
from rand_hex_string import rand_hex_string

class CBCbitflippingHackee:
    def __init__(self, prefix: str, suffix: str):
        self.prefix = prefix
        self.suffix = suffix
        self._key = rand_hex_string(16,16)
        self._transformer = K_eq_v_transformer(seperator=";", equal_sign="=")
    
    def profile_for(self, userdata: str):
        if not self._transformer.accepts(userdata):
            raise ValueError("userdata contains illegal characters")
        
        code = self.prefix + userdata + self.suffix
        return self._transformer.decode(code)