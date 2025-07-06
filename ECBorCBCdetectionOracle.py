from HexString import HexString
from AESinECBdetector import AES_in_ECB_likeliness

def ECB_or_CBC_detection_oracle(input: HexString, limit: int = 10):
    return "ECB" if AES_in_ECB_likeliness(input) < limit else "CBC"
    