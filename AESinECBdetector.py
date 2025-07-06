from HexString import HexString
from typing import Callable
from collections import Counter
from file_loader import load_file_as_string_list

def bytes_list_repeatedness(byte_list: list[bytes], eval_function: Callable[[int],float] = lambda x: x**3):
    result = 0.0
    for x in Counter(byte_list).values():
        result += eval_function(x)
    return result/len(byte_list)

def AES_in_ECB_likeliness(input: HexString, chunk_size: int = 16, eval_function: Callable[[int],float] = lambda x: x**3):
    return bytes_list_repeatedness( [ bytes(input)[i:i+chunk_size] for i in range(0,len(input),chunk_size) ], eval_function)

def find_most_likely_AES_in_ECB_in(inputs: list[HexString], chunk_size: int = 16):
    split_inputs = [ (AES_in_ECB_likeliness(input, chunk_size), input) for input in inputs ]
    return max(split_inputs, key=lambda x: x[0])[1]

if __name__ == "__main__":
    inputs = [ HexString.from_hex_str(s) for s in load_file_as_string_list("AESinECBdetectionProblem.txt") ]
    with open("AESinECBdetectionSolution.txt", 'w') as file:
        print(find_most_likely_AES_in_ECB_in(inputs),file=file,end="")