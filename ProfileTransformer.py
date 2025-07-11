from HexString import HexString
from Profile import Profile
from abc import ABC, abstractmethod
from typing import Callable

class ProfileTransformer(ABC):
    
    def __init__(self, rules: list[Callable[[HexString],bool]] = []) -> None:
        self.rules = rules
    
    @abstractmethod
    def accepts(self, string: HexString) -> bool:
        return all(rule(string) for rule in self.rules)
    
    @abstractmethod
    def encode(self, profile: Profile) -> HexString: pass
    
    @abstractmethod
    def decode(self, code: HexString) -> Profile: pass
    

    