from Profile import Profile
from typing import Callable

class K_eq_v_transformer:
    def __init__(self, rules: list[Callable[[str],bool]]):
        self.rules = rules
    
    def accepts(self, string: str):
        return all(rule(string) for rule in self.rules)
    
    def encode(self, profile: Profile):
        return '&'.join([key+'='+value for key,value in profile.items()])
    
    def decode(self, code: str):
        return Profile({k:v for k,v in [s.split('=') for s in code.split('&')]})
    
class DoesNot:
    
    @classmethod
    def include(cls, bans: str) -> Callable[[str],bool]:
        return lambda s: all(b not in s for b in bans)
    
    