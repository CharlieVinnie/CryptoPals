from HexString import HexString
from EnglishString import EnglishString
from EnglishIdentifier import LetterFrequencyCalculator
from SingleByteXorEncoder import SingleByteXorEncoder

def cipher_single_xored_HexString_and_rank_by_likeliness(hex: HexString):
    result: list[EnglishString] = []
    
    for key in range(256):
        decoded_hex = SingleByteXorEncoder.encode(hex, HexString(key.to_bytes(1,'big')))
        try:
            result.append(decoded_hex.to_english_string())
        except UnicodeDecodeError:
            continue
        
    result.sort(key=LetterFrequencyCalculator.identify)
    return result

def cipher_single_xored_HexString(hex: HexString):
    result_list = cipher_single_xored_HexString_and_rank_by_likeliness(hex)
    if len(result_list) == 0:
        return None
    else:
        result = result_list[-1]
        if LetterFrequencyCalculator.is_bad_text(result):
            return None
        return result
