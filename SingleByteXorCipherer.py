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
    return CipherSingleXoredHexStringAndRankByLikeliness(hex)[-1]

if __name__ == "__main__":
    code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(CipherSingleXoredHexString(HexString.from_str(code)))