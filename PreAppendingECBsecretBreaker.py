from HexString import HexString
from Encryption import Encryption
from NaiveAppendingECBsecretBreaker import naive_appending_ECB_secret_breaker

def A_s(count: int):
    return HexString(b"A" * count)

def get_padding_A_length_for_prefix(oracle: Encryption, max_block_size: int):
    return (int(),int())

def pre_appending_ECB_secret_breaker(oracle: Encryption, max_block_size: int = 64):
    (padding_A_length_for_prefix, prefix_length) = get_padding_A_length_for_prefix(oracle, max_block_size)
    
    class SlicedOracle(Encryption):
        def encrypt(self, input: HexString):
            input = A_s(padding_A_length_for_prefix) + input
            code = oracle.encrypt(input)
            return code[prefix_length:]
    
    return naive_appending_ECB_secret_breaker(SlicedOracle(), max_block_size)
    
    
