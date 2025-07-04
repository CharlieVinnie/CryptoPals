from HexString import HexString
from EnglishString import EnglishString
from EnglishIdentifier import LetterFrequencyCalculator

def CipherSingleXoredHexStringAndRankByLikeliness(hex: HexString):
    result: list[EnglishString] = []
    
    for key in range(256):
        decoded_hex = hex ^ HexString(key.to_bytes(1,'big')*len(hex))
        try:
            result.append(decoded_hex.to_english_string())
        except UnicodeDecodeError:
            continue
        
    result.sort(key=LetterFrequencyCalculator.identify)
    return result

def CipherSingleXoredHexString(hex: HexString):
    result_list = CipherSingleXoredHexStringAndRankByLikeliness(hex)
    if len(result_list) == 0:
        return None
    else:
        return CipherSingleXoredHexStringAndRankByLikeliness(hex)[-1]
