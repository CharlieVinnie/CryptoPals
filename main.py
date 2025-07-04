from Base64String import Base64String
from HexString import HexString
from SingleByteXorCipherer import CipherSingleXoredHexString
from SingleByteXorDetecter import DetectSingleByteXoredHexString

def Convert_hex_to_base64(string: str):
    hex = HexString.from_str(string)
    result = Base64String.from_hex(hex)
    return str(result)

def Fixed_XOR(input1: str, input2: str):
    hex_string1 = HexString.from_str(input1)
    hex_string2 = HexString.from_str(input2)
    result = hex_string1 ^ hex_string2
    return str(result)

def Single_byte_XOR_cipher(input: str):
    hex = HexString.from_str(input)
    result = CipherSingleXoredHexString(hex)
    return str(result)

def Detect_single_character_XOR(input_file: str):
    with open(input_file) as file:
        input_list = [HexString.from_str(string.strip()) for string in file]
    result = DetectSingleByteXoredHexString(input_list)
    return str(result)