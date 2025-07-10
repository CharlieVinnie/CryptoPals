from Profile import Profile
from abc import ABC, abstractmethod
from typing import Callable

class ProfileTransformer(ABC):
    
    def __init__(self, rules: list[Callable[[str],bool]] = []) -> None:
        self.rules = rules
    
    @abstractmethod
    def accepts(self, string: str) -> bool:
        return all(rule(string) for rule in self.rules)
    
    @abstractmethod
    def encode(self, profile: Profile) -> str: pass
    
    @abstractmethod
    def decode(self, code: str) -> Profile: pass
    

    