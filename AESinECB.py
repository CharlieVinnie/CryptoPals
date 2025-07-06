from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from HexString import HexString
from file_loader import load_file_as_single_string

def AES_128_ECB_encrypt(input: HexString, key: HexString):
    cipher = Cipher(algorithms.AES(key.content), modes.ECB(), default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    input = HexString(padder.update(bytes(input)) + padder.finalize())
    result = encryptor.update(input.content) + encryptor.finalize()
    return HexString(result)

def AES_128_ECB_decrypt(input: HexString, key: HexString):
    cipher = Cipher(algorithms.AES(key.content), modes.ECB(), default_backend())
    decryptor = cipher.decryptor()
    result = decryptor.update(input.content) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    result = unpadder.update(result) + unpadder.finalize()
    return HexString(result)

if __name__ == "__main__":
    input = HexString.from_base64_str(load_file_as_single_string("AESinECBnaiveDecode.txt"))
    with open("AESinECBnaiveDecodeSolution.txt", 'w') as file:
        hex_result = AES_128_ECB_decrypt(input, HexString.from_raw_str("YELLOW SUBMARINE"))
        print(hex_result.to_english_string(),file=file,end="")