from file_loader import load_file_as_single_string
from HexString import HexString

class NaiveAppendingECBencryption:
        
    secret_string = load_file_as_single_string("Byte_at_a_time_ECB_decryption_Simple_secret.txt")
    
    def encrypt(self, input: HexString):
        input = input + HexString.from_base64_str(self.secret_string)
        
    