import pytest
import main

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
    

@pytest.mark.parametrize("input", [(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736",
)])
def Challenge_Single_byte_XOR_cipher