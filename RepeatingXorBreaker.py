from HexString import HexString
from SingleByteXorCipherer import cipher_single_xored_HexString
from file_loader import load_file_as_single_string
from Base64String import Base64String

def hamming_distance(a: HexString, b: HexString):
    return sum( (x^y).bit_count() for (x,y) in zip(bytes(a), bytes(b)) )

def break_repeating_key_xor_with_key_size(input: HexString, key_size: int):
    split_input = [ HexString(bytes(input)[i::key_size]) for i in range(key_size) ]
    split_result = [ cipher_single_xored_HexString(s) for s in split_input ]
    return zip(*split_result)

def total_hamming_distance_for_key_size(input: HexString, key_size: int):
    return sum( hamming_distance(HexString(bytes(input)[i:i+key_size]), \
                                  HexString(bytes(input)[i+key_size:i+key_size*2])) for i in range(0,key_size,len(input)-key_size))

# TODO: change sorting key to by only calculated once
def guess_repeating_xor_key_size(input: HexString, max_size: int = 40):
    assert max_size >= 2, "max_size should be at least 2"
    distances = [ (total_hamming_distance_for_key_size(input, i), i) for i in range(2,max_size+1) ]
    distances.sort()
    print(distances)
    return distances[0][1]

if __name__ == "__main__":
    input = load_file_as_single_string("RepeatingXorBreakingProblem.txt")
    print(guess_repeating_xor_key_size(HexString(bytes(Base64String(input))))) # TODO: add Base