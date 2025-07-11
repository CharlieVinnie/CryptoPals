from HexString import HexString
from typing import Callable

class Profile(dict[HexString,HexString]):

    def __getitem__(self, key: str|HexString):
        if isinstance(key, str):
            return super().__getitem__(HexString.from_raw_str(key))
        else:
            return super().__getitem__(key)
    

class ProfileCreator:
    def __init__(self, generated_fields: dict[HexString, Callable[[],HexString]], input_fields: set[HexString]) :
        self.generated_fields = generated_fields
        self.input_fields = input_fields
        
        if input_fields.intersection(generated_fields.keys()):
            raise ValueError("input_fields and generated_fields overlap")
        
    def create(self, input: dict[HexString,HexString]):
        profile: dict[HexString,HexString] = {}
        if input.keys() != self.input_fields:
            raise ValueError("input fields do not match")
        
        for key in self.input_fields:
            profile[key] = input[key]
        for key,generation in self.generated_fields.items():
            profile[key] = generation()
            
        return Profile(profile)
    