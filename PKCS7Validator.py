from HexString import HexString

def PKCS_7_validate(input: HexString):
    if len(input) % 16 != 0:
        raise ValueError("Invalid input length")
    
    if not input:
        return input
    
    pad = input[-1]
    if pad > 16 or pad == 0:
        raise ValueError("Invalid padding")
    
    if input[-pad:] != HexString(bytes([pad] * pad)):
        raise ValueError("Invalid padding")
    
    return input[:-pad]