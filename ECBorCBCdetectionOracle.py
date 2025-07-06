from HexString import HexString
from AESinECBdetector import AES_in_ECB_likeliness

def ECB_or_CBC_detection_oracle(input: HexString, limit: float = 1+1e-10):
    return "ECB" if AES_in_ECB_likeliness(input) >= limit else "CBC"
    