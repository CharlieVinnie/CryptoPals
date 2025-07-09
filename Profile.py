from typing import Callable

Profile = dict[str,str]

class ProfileCreator:
    def __init__(self, generated_fields: dict[str, Callable[[],str]], input_fields: set[str]) :
        self.generated_fields = generated_fields
        self.input_fields = input_fields
        
        if input_fields.intersection(generated_fields.keys()):
            raise ValueError("input_fields and generated_fields overlap")
        
    def create(self, input: dict[str,str]):
        profile: dict[str,str] = {}
        if input.keys() != self.input_fields:
            raise ValueError("input fields do not match")
        
        for key in self.input_fields:
            profile[key] = input[key]
        for key,generation in self.generated_fields.items():
            profile[key] = generation()
            
        return profile
    