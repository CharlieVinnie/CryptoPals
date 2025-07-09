from HexString import HexString
from AESencrypt import AESencrypt
from AESdecrypt import AESdecrypt
from block_split import block_split
from file_loader import load_file_as_single_string
from paddingPKCS7 import add_padding_PKCS_7, remove_padding_PKCS_7

def AES_128_CBC_encrypt(input: HexString, key: HexString, iv: HexString):
    result = iv
    for block in block_split(add_padding_PKCS_7(input, 16), 16):
        result += AESencrypt(block ^ result[-16:], key)
    return result

def AES_128_CBC_decrypt(input: HexString, key: HexString, iv: HexString):
    result = HexString(bytes())
    blocks = block_split(input, 16)
    for (block, prev_block) in reversed( list(zip(blocks, [iv]+blocks[:-1])) ):
        this_result = AESdecrypt(block, key) ^ prev_block
        result = this_result + result
    return remove_padding_PKCS_7(result)
        

if __name__ == "__main__":
    input = HexString.from_base64_str(load_file_as_single_string("AESinCBCnaiveDecode.txt"))
    with open("AESinCBCnaiveDecodeSolution.txt", 'w') as file:
        result = AES_128_CBC_decrypt(input, HexString.from_raw_str("YELLOW SUBMARINE"), HexString((0).to_bytes(16, 'big')))
        print(result.to_english_string(),file=file,end="")