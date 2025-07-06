from AESinECB import AES_128_ECB_encrypt
from AESinCBC import AES_128_CBC_encrypt
from HexString import HexString
from random import randint, Random


def random_ECB_or_CBC_encrypt(input: HexString, rng: Random = Random()):
    def rand_hex_string(min_length: int, max_length: int):
        length = randint(min_length, max_length)
        return HexString(bytes([rng.randint(0, 255) for _ in range(length)]))
    
    input = rand_hex_string(5,10) + input + rand_hex_string(5,10)
    
    if rng.randint(0,1) == 0:
        result = AES_128_ECB_encrypt(input, rand_hex_string(16,16))
        return (result, "ECB")
    else:
        result = AES_128_CBC_encrypt(input, rand_hex_string(16,16), rand_hex_string(16,16))
        return (result, "CBC")
