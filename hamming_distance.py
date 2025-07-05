from HexString import HexString

def hamming_distance(a: HexString, b: HexString):
    return sum( (x^y).bit_count() for (x,y) in zip(bytes(a), bytes(b)) )
