from Base64String import Base64String
from HexString import HexString

def Convert_hex_to_base64(string: str):
    hex = HexString.from_str(string)
    result = Base64String.from_hex(hex)
    return str(result)

def Fixed_XOR(input1: str, input2: str):
    hex_string1 = HexString.from_str(input1)
    hex_string2 = HexString.from_str(input2)
    result = hex_string1 ^ hex_string2
    return str(result)