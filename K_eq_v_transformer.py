from Profile import Profile
from typing import Callable
from ProfileTransformer import ProfileTransformer
from TransformerRules import DoesNot

class K_eq_v_transformer(ProfileTransformer):
    
    def __init__(self, seperator: str, equal_sign: str, rules: list[Callable[[str],bool]] = []):
        self.seperator = seperator
        self.equal_sign = equal_sign
        rules.append(DoesNot.include(seperator))
        rules.append(DoesNot.include(equal_sign))
        super().__init__(rules)
    
    def accepts(self, string: str):
        return super().accepts(string)
    
    def encode(self, profile: Profile):
        return self.seperator.join([key+self.equal_sign+value for key,value in profile.items()])
    
    def decode(self, code: str):
        return Profile({k:v for k,v in [s.split(self.equal_sign) for s in code.split(self.seperator)]})
    

    