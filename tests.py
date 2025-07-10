import pytest
from CBCbitflippingHackee import CBCbitflippingHackee
from PreAppendingECBencryption import PreAppendingECBencryption
import main
from file_loader import load_file_as_it_is, load_file_as_single_string
import random
from RandomECBorCBCencryptor import random_ECB_or_CBC_encrypt
from HexString import HexString
from NaiveAppendingECBencryption import NaiveAppendingECBencryption
from Base64String import Base64String
from ECBkeqvHackee import ECBkeqvHackee
import re

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
    

@pytest.mark.parametrize("input_file, output_file",[(
    "AESinECBnaiveDecode.txt",
    "AESinECBnaiveDecodeSolution.txt",
)])
def Challenge_AES_in_ECB_mode(input_file: str, output_file: str):
    assert main.AES_in_ECB_mode(input_file) == load_file_as_it_is(output_file)
    

@pytest.mark.parametrize("input_file, output_file",[(
    "AESinECBdetectionProblem.txt",
    "AESinECBdetectionSolution.txt",
)])
def Challenge_Detect_AES_in_ECB_mode(input_file: str, output_file: str):
    assert main.Detect_AES_in_ECB_mode(input_file) == load_file_as_it_is(output_file)
    

@pytest.mark.parametrize("input,padding_size,output",[(
    "YELLOW SUBMARINE",
    20,
    "YELLOW SUBMARINE\x04\x04\x04\x04",
)])
def Challenge_Implement_PKCS_7_padding(input: str, padding_size: int, output: str):
    assert main.Implement_PKCS_7_padding(input, padding_size) == output
    

@pytest.mark.parametrize("input_file,output_file",[(
    "AESinCBCnaiveDecode.txt",
    "AESinCBCnaiveDecodeSolution.txt",
)])
def Challenge_Implement_CBC_mode(input_file: str, output_file: str):
    assert main.AES_in_CBC_mode(input_file) == load_file_as_it_is(output_file)
    

@pytest.mark.parametrize("seed, rounds", [(330312,30)])
@pytest.mark.parametrize("english_text_file",[
    "English_text/1.txt",
    "English_text/2.txt",
    "English_text/3.txt",
])
def Challenge_ECB_CBC_detection_oracle(seed: int, rounds: int, english_text_file: str):
    rng = random.Random(seed)
    for _ in range(rounds):
        text = load_file_as_it_is(english_text_file)
        hex = HexString.from_raw_str(text)
        (input, type) = random_ECB_or_CBC_encrypt(hex, rng)
        assert main.ECB_CBC_detection_oracle(input) == type
        

@pytest.mark.parametrize("secret_file",["Byte_at_a_time_ECB_decryption_problem.txt"])
def Challenge_Byte_at_a_time_ECB_decryption_simple(secret_file: str):
    secret_string_in_base64 = load_file_as_single_string(secret_file)
    oracle = NaiveAppendingECBencryption.create(HexString.from_base64_str(secret_string_in_base64))
    assert main.Byte_at_a_time_ECB_decryption_simple(oracle) == Base64String.from_base64_str(secret_string_in_base64)


@pytest.mark.parametrize("email",["1@2.com"])
def test_ECBkeqvHackeeAcceptsValidEmail(email: str):
    hackee = ECBkeqvHackee()
    profile = hackee.decrypt_profile(hackee.profile_for(email))
    assert profile["email"] == email
    assert profile["role"] == "user"
    

@pytest.mark.parametrize("email",["1&2.com","1=2.com"])
def test_ECBkeqvHackeeRejectsInvalidEmail(email: str):
    hackee = ECBkeqvHackee()
    with pytest.raises(ValueError):
        hackee.profile_for(email)


@pytest.mark.parametrize("email",["1@2.com"])
def test_ECBkeqvHackeeEncodesInCorrectWay(email: str):
    hackee = ECBkeqvHackee()
    code = hackee._encode_profile_with_email(email) # pyright: ignore [reportPrivateUsage]
    assert re.match(rf"^email={email}&uid=[0-9]+&role=user$", code)


def Challenge_ECB_cut_and_paste():
    hackee = ECBkeqvHackee()
    encrypted_profile = main.ECB_cut_and_paste(hackee)
    profile = hackee.decrypt_profile(encrypted_profile)
    assert profile["role"] == "admin"
    
@pytest.mark.parametrize("secret_file",["Byte_at_a_time_ECB_decryption_problem.txt"])
def Challenge_Byte_at_a_time_ECB_decryption_harder(secret_file: str):
    secret_string_in_base64 = load_file_as_single_string(secret_file)
    oracle = PreAppendingECBencryption.create(HexString.from_base64_str(secret_string_in_base64))
    assert main.Byte_at_a_time_ECB_decryption_harder(oracle) == Base64String.from_base64_str(secret_string_in_base64)
    

@pytest.mark.parametrize("input,result",[
    (b"ICE ICE BABY\x04\x04\x04\x04", b"ICE ICE BABY"),
    (b"ICE ICE BABY\x05\x05\x05\x05", None),
    (b"ICE ICE BABY\x01\x02\x03\x04", None),
])
def Challenge_PKCS_7_padding_validation(input: bytes, result: None|bytes):
    if result is None:
        with pytest.raises(ValueError):
            main.PKCS_7_padding_validation(input)
    else:
        assert main.PKCS_7_padding_validation(input) == result
        

@pytest.mark.parametrize("comment1,comment2",[(
    r"cooking%20MCs",
    r"%20like%20a%20pound%20of%20bacon",
)])
@pytest.mark.parametrize("userdata",["123","user","user123","123user"])
def test_CBCbitflippingHackeeAcceptsValidUserdata(comment1: str, comment2: str, userdata: str):
    prefix = f"comment1={comment1};userdata="
    suffix = f";comment2={comment2}"
    hackee = CBCbitflippingHackee(prefix, suffix)
    profile = hackee.profile_for(userdata)
    assert profile == {"comment1": comment1, "comment2": comment2, "userdata": userdata}


@pytest.mark.parametrize("prefix,suffix",[(
    r"comment1=cooking%20MCs;userdata=",
    r";comment2=%20like%20a%20pound%20of%20bacon",
)])
def Challenge_CBC_bitflipping_attacks(prefix: str, suffix: str):
    hackee = CBCbitflippingHackee(prefix, suffix)
    userdata = main.CBC_bitflipping_attacks(hackee)
    profile = hackee.profile_for(userdata)
    assert profile["admin"] == "true"
    