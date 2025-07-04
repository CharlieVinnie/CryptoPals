from HexString import HexString

def mask_generator(key: str):
    for i in range(len(key)):
        yield key[i]

def repeating_key_xor_encode(input: str, key: str):
    pass