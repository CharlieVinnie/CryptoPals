from hex_base64_convert import hex_to_base64, HexString

def Convert_hex_to_base64(string: str):
    result = hex_to_base64(HexString(string))
    return result.to_string()