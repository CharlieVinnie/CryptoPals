import pytest
import main

@pytest.mark.parametrize("hex_input, base64_output", [(
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d",
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
)])
def Challenge_Convert_hex_to_base64(hex_input: str, base64_output: str):
    assert main.Convert_hex_to_base64(hex_input) == base64_output