from HexString import HexString

def block_split(input: HexString, block_size: int):
    if len(input) % block_size != 0:
        raise ValueError("Input length should be a multiple of block size")
    return [input[i:i+block_size] for i in range(0, len(input), block_size)]