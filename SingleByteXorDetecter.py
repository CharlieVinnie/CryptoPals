from SingleByteXorCipherer import CipherSingleXoredHexString
from HexString import HexString
from EnglishIdentifier import LetterFrequencyCalculator

def DetectSingleByteXoredHexString(input_list: list[HexString]):
    decoded_list = [result for hex in input_list if (result := CipherSingleXoredHexString(hex)) != None]
    print(decoded_list)
    return max(decoded_list, key=LetterFrequencyCalculator.identify)
