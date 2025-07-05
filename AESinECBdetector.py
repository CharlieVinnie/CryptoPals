from HexString import HexString
from typing import Callable
from collections import Counter
from file_loader import load_file_as_string_list

def bytes_list_repeatedness(byte_list: list[bytes], eval_function: Callable[[int],float] = lambda x: x**3):
    result = 0.0
    for x in Counter(byte_list).values():
        result += eval_function(x)
    return result/len(byte_list)

def find_most_likely_AES_in_ECB_in(inputs: list[HexString], chunk_size: int = 16):
    def splitter(s: HexString):
        return [ bytes(s)[i:i+chunk_size] for i in range(0,len(s),chunk_size) ]
    split_inputs = [ (splitter(input), input) for input in inputs ]
    return max(split_inputs, key=lambda x: bytes_list_repeatedness(x[0]))[1]


if __name__ == "__main__":
    inputs = [ HexString.from_hex_str(s) for s in load_file_as_string_list("AESinECBdetectionProblem.txt") ]
    with open("AESinECBdetectionSolution.txt", 'w') as file:
        print(find_most_likely_AES_in_ECB_in(inputs),file=file,end="")