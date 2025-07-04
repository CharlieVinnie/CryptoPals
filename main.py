from hex_base64_convert import hex_to_base64, str_to_HexString

def Convert_hex_to_base64(string: str):
    result = hex_to_base64(str_to_HexString(string))
    return result.to_string()

def Fixed_XOR(input1: str, input2: str):
    hex_string1 = str_to_HexString(input1)
    hex_string2 = str_to_HexString(input2)
    result = hex_string1 ^ hex_string2
    return result.to_string()