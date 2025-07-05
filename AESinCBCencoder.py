from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from HexString import HexString

def add_padding_PKCS_7(hex: HexString, size: int):
    padding_size = size - len(hex) % size
    return hex + HexString(padding_size.to_bytes(1, 'big')*padding_size)