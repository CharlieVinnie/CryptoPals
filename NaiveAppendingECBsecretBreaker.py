from Encryption import Encryption
from HexString import HexString

def A_s(count: int):
    return HexString(b"A" * count)

def try_block_size(oracle: Encryption, block_size: int):
    code_1 = oracle.encrypt(A_s(0))
    code_2 = oracle.encrypt(A_s(block_size))
    return code_1 == code_2[block_size:]

def crack_block_size(oracle: Encryption, max_block_size: int):
    try:
        block_size = next( block_size for block_size in range(1, max_block_size+1) if try_block_size(oracle, block_size) )
    except StopIteration:
        raise ValueError("Unable to crack block size")
    
    code_1 = oracle.encrypt(A_s(block_size))
    code_2 = oracle.encrypt(A_s(block_size*2))
    if code_1[:block_size] * 2 != code_2[:block_size*2]:
        raise ValueError("Unable to crack block size")
    
    return block_size

def calculate_secret_length(oracle: Encryption, block_size: int):
    padding_length = next( i for i in range(1, block_size) if len(oracle.encrypt(A_s(i))) != len(oracle.encrypt(A_s(0))) )
    return len(oracle.encrypt(A_s(0))) - padding_length

def try_next_byte(oracle: Encryption, secret: HexString, block_size: int, byte: bytes):
    index = len(secret)
    A_padding_length = block_size - index%block_size - 1
    A_padding = A_s(A_padding_length)
    code_1 = oracle.encrypt(A_padding)
    code_2 = oracle.encrypt(A_padding + secret + HexString(byte))
    length = A_padding_length + index + 1
    return code_1[:length] == code_2[:length]
    

def crack_next_byte(oracle: Encryption, secret: HexString, block_size: int):
    try:
        next_byte = next( byte for byte in range(256) if try_next_byte(oracle, secret, block_size, byte.to_bytes(1, "big")) )
        return next_byte.to_bytes(1, "big")
    except StopIteration:
        raise ValueError("Unable to crack secret")

def naive_appending_ECB_secret_breaker(oracle: Encryption, max_block_size: int = 64):
    try:
        block_size = crack_block_size(oracle, max_block_size)
        print(f"Block size: {block_size}")
    except ValueError:
        raise ValueError("oracle is not encrypted with NaiveAppendingECBencryption algorithm")
    
    secret_length = calculate_secret_length(oracle, block_size)
    print(f"Secret length: {secret_length}")
    secret = HexString()
    
    for _ in range(secret_length):
        secret += HexString(crack_next_byte(oracle, secret, block_size))
    
    return secret