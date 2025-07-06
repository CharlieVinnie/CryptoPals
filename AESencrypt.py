from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from HexString import HexString

def AESencrypt(input: HexString, key: HexString):
    cipher = Cipher(algorithms.AES(bytes(key)), modes.ECB(), default_backend())
    encryptor = cipher.encryptor()
    result = encryptor.update(bytes(input)) + encryptor.finalize()
    return HexString(result)