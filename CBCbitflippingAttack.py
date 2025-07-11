from HexString import H, HexString
from CBCbitflippingHackee import CBCbitflippingHackee
import random
import string

def A_s(count: int):
    return HexString(b"A" * count)

def CBC_bitflipping_attack(hackee: CBCbitflippingHackee, max_attack_rounds: int = 2000):
    goal = ";admin=true"
    
    prefix = hackee.prefix()
    pad_len = 16*2 - len(prefix)%16
    
    for _ in range(max_attack_rounds):
        rand_string = H("".join(random.choices(string.ascii_letters + string.digits, k=pad_len+len(goal))))
        try:
            code = hackee.profile_for(rand_string)
        except Exception as e:
            print(e.args[0])
            continue
        
        goal_pos = len(prefix) + pad_len
        
        tamper = rand_string[pad_len:] ^ HexString.from_raw_str(goal)
        mask = HexString(bytes(goal_pos-16)) + tamper + HexString(bytes(len(code)-(goal_pos-16+len(goal))))
        code ^= mask
        
        try:
            hackee.decrypt_profile(code)
            return code
        except Exception as e:
            print(e.args[0])
            continue
        
    raise ValueError("CBC bitflipping attack failed")