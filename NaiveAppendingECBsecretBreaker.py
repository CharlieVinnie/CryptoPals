from Encryption import Encryption
from HexString import HexString

def try_block_size(oracle: Encryption, block_size: int):
    return True

def crack_block_size(oracle: Encryption, max_block_size: int):
    return next( block_size for block_size in range(1, max_block_size+1) if try_block_size(oracle, block_size) )

def calculate_secret_length(oracle: Encryption, block_size: int):
    return int()

def try_next_byte(oracle: Encryption, secret: HexString, block_size: int, byte: bytes):
    return True

def crack_next_byte(oracle: Encryption, secret: HexString, block_size: int):
    try:
        next_byte = next( byte for byte in range(256) if try_next_byte(oracle, secret, block_size, byte.to_bytes(1, "big")) )
        return next_byte.to_bytes(1, "big")
    except StopIteration:
        raise ValueError("Unable to crack secret")

def naive_appending_ECB_secret_breaker(oracle: Encryption, max_block_size: int = 64):
    try:
        block_size = crack_block_size(oracle, max_block_size)
    except ValueError:
        raise ValueError("oracle is not encrypted with NaiveAppendingECBencryption algorithm")
    
    secret_length = calculate_secret_length(oracle, block_size)
    secret = HexString()
    
    for _ in range(secret_length):
        secret += HexString(crack_next_byte(oracle, secret, block_size))
    
    return secret