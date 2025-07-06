from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from HexString import HexString

def AESdecrypt(input: HexString, key: HexString):
    cipher = Cipher(algorithms.AES(bytes(key)), modes.ECB(), default_backend())
    decryptor = cipher.decryptor()
    result = decryptor.update(bytes(input)) + decryptor.finalize()
    return HexString(result)