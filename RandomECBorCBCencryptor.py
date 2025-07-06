from AESinECB import AES_128_ECB_encrypt
from AESinCBC import AES_128_CBC_encrypt
from HexString import HexString
from random import Random
from rand_hex_string import rand_hex_string


def random_ECB_or_CBC_encrypt(input: HexString, rng: Random = Random()):
    input = rand_hex_string(5,10,rng) + input + rand_hex_string(5,10,rng)
    
    if rng.randint(0,1) == 0:
        result = AES_128_ECB_encrypt(input, rand_hex_string(16,16,rng))
        return (result, "ECB")
    else:
        result = AES_128_CBC_encrypt(input, rand_hex_string(16,16,rng), rand_hex_string(16,16,rng))
        return (result, "CBC")
