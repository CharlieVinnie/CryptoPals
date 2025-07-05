import pytest
import main
from file_loader import load_file_as_it_is

@pytest.mark.parametrize("hex_input, base64_output", [(
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d",
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
)])
def Challenge_Convert_hex_to_base64(hex_input: str, base64_output: str):
    assert main.Convert_hex_to_base64(hex_input) == base64_output


@pytest.mark.parametrize("input1, input2, xor_output", [(
    "1c0111001f010100061a024b53535009181c",
    "686974207468652062756c6c277320657965",
    "746865206b696420646f6e277420706c6179",
)])
def Challenge_Fixed_XOR(input1: str, input2: str, xor_output: str):
    assert main.Fixed_XOR(input1,input2) == xor_output
    

@pytest.mark.parametrize("input, output", [(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736",
    "Cooking MC's like a pound of bacon",
)])
def Challenge_Single_byte_XOR_cipher(input: str, output: str):
    assert main.Single_byte_XOR_cipher(input) == output
    

@pytest.mark.parametrize("input_file, output", [(
    "SingleByteXorDetectProblem.txt",
    "Now that the party is jumping\n",
)])
def Challenge_Detect_single_character_XOR(input_file: str, output: str):
    assert main.Detect_single_character_XOR(input_file) == output
    

@pytest.mark.parametrize("input, key, output",[(
    "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
    "ICE",
    "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a"\
        "282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f",
)])
def Challenge_Implement_repeating_key_XOR(input: str, key: str, output: str):
    assert main.Implement_repeating_key_XOR(input, key) == output
    

@pytest.mark.parametrize("a,b,dist", [("this is a test", "wokka wokka!!!",37)])
def test_hamming_distance(a: str, b: str, dist: int):
    assert main.hamming_distance(main.HexString.from_raw_str(a), main.HexString.from_raw_str(b)) == dist
    

@pytest.mark.parametrize("input_file, output_file",[(
    "RepeatingKeyXorBreakingProblem.txt",
    "RepeatingKeyXorBreakingSolution.txt",
)])
def Challenge_Break_repeating_key_XOR(input_file: str, output_file: str):
    assert main.Break_repeating_key_XOR(input_file) == load_file_as_it_is(output_file)