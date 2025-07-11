from HexString import HexString
from random import Random

# TODO: refactor omit max_length
def rand_hex_string(min_length: int, max_length: int, rng: Random = Random()):
    length = rng.randint(min_length, max_length)
    return HexString(bytes([rng.randint(0, 255) for _ in range(length)]))