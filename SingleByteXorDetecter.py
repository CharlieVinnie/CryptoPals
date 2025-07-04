from SingleByteXorCipherer import CipherSingleXoredHexString, CipherSingleXoredHexStringAndRankByLikeliness
from HexString import HexString
from EnglishIdentifier import LetterFrequencyCalculator

def DetectSingleByteXoredHexString(input_list: list[HexString]):
    decoded_list = [result for hex in input_list if (result := CipherSingleXoredHexString(hex)) != None]
    print(decoded_list)
    return max(decoded_list, key=LetterFrequencyCalculator.identify)

if __name__ == "__main__":
    with open("SingleByteXorDetectProblem.txt") as file:
        input_list = [HexString.from_str(string.strip()) for string in file]
        
    for hex in input_list:
        # print(hex)
        print(CipherSingleXoredHexStringAndRankByLikeliness(hex))
    
    result = DetectSingleByteXoredHexString(input_list)
    
    print(result)