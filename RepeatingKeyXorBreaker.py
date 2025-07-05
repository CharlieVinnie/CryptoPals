from HexString import HexString
from SingleByteXorCipherer import cipher_single_xored_HexString
from file_loader import load_file_as_single_string
from EnglishIdentifier import LetterFrequencyCalculator
from EnglishString import EnglishString
from itertools import chain, zip_longest

def hamming_distance(a: HexString, b: HexString):
    return sum( (x^y).bit_count() for (x,y) in zip(bytes(a), bytes(b)) )

# TODO: make EnglishString contain illegal strings
def break_repeating_key_xor_with_key_size(input: HexString, key_size: int):
    split_input = [ HexString(bytes(input)[i::key_size]) for i in range(key_size) ]
    split_result = [ cipher_single_xored_HexString(s) for s in split_input ]
    if None in split_result:
        return None
    split_result = [s for s in split_result if s != None]
    strings = chain(*zip_longest(*split_result,fillvalue=''))
    return EnglishString("".join(strings))

def total_hamming_distance_for_key_size(input: HexString, key_size: int):
    return sum( hamming_distance(HexString(bytes(input)[i:i+key_size]), \
                                  HexString(bytes(input)[i+key_size:i+key_size*2])) for i in range(0,len(input)-key_size,key_size) )

# TODO: change sorting key to by only calculated once
def guess_repeating_xor_key_size(input: HexString, max_size: int = 5):
    assert max_size >= 2, "max_size should be at least 2"
    distances = [ (total_hamming_distance_for_key_size(input, i), i) for i in range(2,max_size+1) ]
    distances.sort()
    return [k for (_,k) in distances]

def break_repeating_key_xor(input: HexString, max_size: int = 40, check_key_size_count: int = 40):
    key_sizes = guess_repeating_xor_key_size(input, max_size)
    key_sizes = key_sizes[:check_key_size_count]
    result = [break_repeating_key_xor_with_key_size(input, key_size) for key_size in key_sizes]
    result = [r for r in result if r != None]
    return max(result, key=LetterFrequencyCalculator.identify)

if __name__ == "__main__":
    input = load_file_as_single_string("RepeatingKeyXorBreakingProblem.txt")
    with open("RepeatingKeyXorBreakingSolution.txt", 'w') as file:
        print(break_repeating_key_xor(HexString.from_base64_str(input)),file=file,end="")
    