from HexString import HexString

def add_padding_PKCS_7(hex: HexString, size: int):
    padding_size = size - len(hex) % size
    return hex + HexString(padding_size.to_bytes(1, 'big')*padding_size)

def remove_padding_PKCS_7(hex: HexString):
    padding_size = hex[-1]
    return hex[:-padding_size]
