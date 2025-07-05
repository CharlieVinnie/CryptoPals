from Base64String import Base64String
from HexString import HexString
from SingleByteXorCipherer import cipher_single_xored_HexString
from SingleByteXorDetecter import detect_single_byte_xored_HexString
from RepeatingKeyXorEncoder import RepeatingKeyXorEncoder
from RepeatingKeyXorBreaker import hamming_distance # type: ignore
from file_loader import load_file_as_string_list, load_file_as_single_string
from RepeatingKeyXorBreaker import break_repeating_key_xor
from AESDecoder import AES_128_ECB_decode

def Convert_hex_to_base64(string: str):
    hex = HexString.from_hex_str(string)
    result = Base64String.from_hex(hex)
    return str(result)

def Fixed_XOR(input1: str, input2: str):
    hex_string1 = HexString.from_hex_str(input1)
    hex_string2 = HexString.from_hex_str(input2)
    result = hex_string1 ^ hex_string2
    return str(result)

def Single_byte_XOR_cipher(input: str):
    hex = HexString.from_hex_str(input)
    result = cipher_single_xored_HexString(hex)
    return str(result)

def Detect_single_character_XOR(input_file: str):
    input_list = [HexString.from_hex_str(string) for string in load_file_as_string_list(input_file)]
    result = detect_single_byte_xored_HexString(input_list)
    return str(result)

def Implement_repeating_key_XOR(input: str, key: str):
    result = RepeatingKeyXorEncoder.encode(HexString.from_raw_str(input), HexString.from_raw_str(key))
    return str(result)

def Break_repeating_key_XOR(input_file: str):
    input = HexString.from_base64_str(load_file_as_single_string(input_file))
    result = break_repeating_key_xor(input)
    return str(result)

def AES_in_ECB_mode(input_file: str):
    input = HexString.from_base64_str(load_file_as_single_string(input_file))
    result = AES_128_ECB_decode(input, HexString.from_raw_str("YELLOW SUBMARINE"))
    return str(result.to_english_string())