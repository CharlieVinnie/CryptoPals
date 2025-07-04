from SingleByteXorCipherer import cipher_single_xored_HexString
from HexString import HexString
from EnglishIdentifier import LetterFrequencyCalculator

def detect_single_byte_xored_HexString(input_list: list[HexString]):
    decoded_list = [result for hex in input_list if (result := cipher_single_xored_HexString(hex)) != None]
    print(decoded_list)
    return max(decoded_list, key=LetterFrequencyCalculator.identify)
