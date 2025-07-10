from HexString import HexString
from Encryption import Encryption
from NaiveAppendingECBsecretBreaker import naive_appending_ECB_secret_breaker
from rand_hex_string import rand_hex_string

def A_s(count: int):
    return HexString(b"A" * count)

def all_equal(t: tuple[HexString,...]):
    return all( x == t[0] for x in t )

def lcp(strings: list[HexString]):
    zips = list(zip(*strings))
    return next((i for i in range(len(zips)) if not all_equal(zips[i])), len(zips))

def get_fixed_prefix_length(oracle: Encryption, length: int, random_check_rounds: int = 20):
    return lcp([ oracle.encrypt(A_s(length)+rand_hex_string(length,length)) for _ in range(random_check_rounds) ])

def pre_appending_ECB_secret_breaker(oracle: Encryption, max_block_size: int = 64, random_check_rounds: int = 20):
    length = len(oracle.encrypt(A_s(0)))
    
    fixed_prefix_length = get_fixed_prefix_length(oracle, length, random_check_rounds)
    
    print(f"Fixed prefix length: {fixed_prefix_length}")
    
    try:
        padding_A_length = 1 + next( i for i in range(length,0,-1) if get_fixed_prefix_length(oracle, i, random_check_rounds) != fixed_prefix_length )
    except StopIteration:
        raise ValueError("Unable to determine padding A length: oracle is not encrypted with PreAppendingECBencryption algorithm")
    
    assert fixed_prefix_length % 16 == 0, "random check rounds is not enough"
    prefix_length = fixed_prefix_length // 16
    
    print(f"Padding A length: {padding_A_length}")
    print(f"Prefix length: {prefix_length}")
    
    class SlicedOracle(Encryption):
        def encrypt(self, input: HexString):
            input = A_s(padding_A_length) + input
            code = oracle.encrypt(input)
            return code[fixed_prefix_length:]
    
    try:
        return naive_appending_ECB_secret_breaker(SlicedOracle(), max_block_size)
    except ValueError:
        raise ValueError("Unable to crack secret: oracle is not encrypted with PreAppendingECBencryption algorithm")
    
    
