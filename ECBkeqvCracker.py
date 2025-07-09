from ECBkeqvHackee import ECBkeqvHackee
from HexString import HexString
from Profile import Profile
from random import randint
from paddingPKCS7 import add_padding_PKCS_7

def A_s(count: int):
    return 'A'*count

def ECBkeqvCracker(hackee: ECBkeqvHackee):
    while True:
        count = randint(1,16)
        encrypted_profile = hackee.profile_for(A_s(count))
        profile = hackee.decrypt_profile(encrypted_profile)
        prefix_length = len("email="+profile["email"]+"&uid="+profile["uid"]+"&role=")
        if prefix_length%16==0:
            break
    
    prefix = encrypted_profile[:prefix_length]
    
    a_s = A_s(16-len("email="))
    admin = add_padding_PKCS_7(HexString.from_raw_str("admin"), 16).to_raw_str()
    
    encrypted_profile = hackee.profile_for(a_s+admin)
    suffix = encrypted_profile[16:32]
    
    return prefix + suffix