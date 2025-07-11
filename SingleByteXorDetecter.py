from SingleByteXorCipherer import cipher_single_xored_HexString
from HexString import HexString
from EnglishIdentifier import LetterFrequencyCalculator

def detect_single_byte_xored_HexString(input_list: list[HexString]):
    decoded_list = [cipher_single_xored_HexString(hex) for hex in input_list]
    print(decoded_list)
    return max(decoded_list, key=LetterFrequencyCalculator.identify)
