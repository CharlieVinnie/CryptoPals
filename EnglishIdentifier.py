from __future__ import annotations
from abc import ABC, abstractmethod
from EnglishString import EnglishString
from functools import total_ordering

@total_ordering
class IdentifyResult(ABC):
    @abstractmethod
    def __lt__(self, other: IdentifyResult) -> bool: pass

class EnglishIdentifier(ABC):
    
    @classmethod
    @abstractmethod
    def identify(cls, text: EnglishString) -> IdentifyResult: pass


class LetterFrequencyIdentifyResult(IdentifyResult):

    def __init__(self, likeliness: float, strange_characters: int, bad_text: bool):
        self.likeliness = likeliness
        self.strange_characters = strange_characters
        self.bad_text = bad_text

    @classmethod
    def bad_result(cls):
        return LetterFrequencyIdentifyResult(0.0, 0, True)
        
    def __lt__(self, other: IdentifyResult):
        if not isinstance(other, LetterFrequencyIdentifyResult):
            return NotImplemented
        
        if self.bad_text != other.bad_text:
            return self.bad_text
        
        if self.strange_characters != other.strange_characters:
            return self.strange_characters > other.strange_characters
        
        return self.likeliness < other.likeliness

class LetterFrequencyCalculator(EnglishIdentifier):
    
    english_letter_frequency: list[float] = []
    
    @classmethod
    def load_english_letter_frequency(cls):
        if cls.english_letter_frequency: return
        
        cls.english_letter_frequency = [0 for _ in range(26)]
        
        with open('letter_frequency.txt') as file:
            for (letter,_,freq,_) in zip(*[file]*4):
                letter: str
                freq: str
                cls.english_letter_frequency[ord(letter.strip().lower()) - ord('a')] = float(freq)
    
    @classmethod
    def likeliness(cls, letter_frequency: list[float]) -> float:
        cls.load_english_letter_frequency()
        letter_frequency_sum = sum(letter_frequency)
        return sum(abs(cls.english_letter_frequency[i] - letter_frequency[i]/letter_frequency_sum) for i in range(26))
    
    @classmethod
    def identify(cls, text: EnglishString) -> LetterFrequencyIdentifyResult:
        letter_frequency = [0.0 for _ in range(26)]
        strange_characters = 0
        bad_text = False
        
        for letter in text:
            if letter == ' ':
                continue
            elif letter.isalpha():
                letter_frequency[ord(letter.lower()) - ord('a')] += 1.0
            elif not letter.isprintable():
                bad_text = True
            else:
                strange_characters += 1
        
        if bad_text or sum(letter_frequency) == 0:
            return LetterFrequencyIdentifyResult.bad_result()
        
        return LetterFrequencyIdentifyResult(cls.likeliness(letter_frequency), strange_characters, False)
        
        
        
    
    