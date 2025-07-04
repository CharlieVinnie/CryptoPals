from abc import ABC, abstractmethod
import math

class EnglishIndentifier(ABC):
    
    @abstractmethod
    @classmethod
    def identify(cls, text: str) -> float: pass


class LetterFrequencyCalculator(EnglishIndentifier):
    
    english_letter_frequency: list[float] = []
    
    @classmethod
    def load_english_letter_frequency(cls):
        if cls.english_letter_frequency: return
        
        cls.english_letter_frequency = [0 for _ in range(26)]
        
        with open('letter_frequency.txt') as file:
            for (letter,_,freq,_) in zip(*[file]*4):
                letter: str
                freq: float
                cls.english_letter_frequency[ord(letter.lower()) - ord('a')] = freq
    
    @classmethod
    def likeliness(cls, letter_frequency: list[float]) -> float:
        cls.load_english_letter_frequency()
        letter_frequency_sum = sum(letter_frequency)
        return sum(abs(cls.english_letter_frequency[i] - letter_frequency[i]/letter_frequency_sum) for i in range(26))
    
    @classmethod
    def identify(cls, text: str) -> float:
        letter_frequency = [0.0 for _ in range(26)]
        strange_characters = 0
        
        for letter in text:
            if letter.isspace():
                continue
            elif letter.isalpha():
                letter_frequency[ord(letter.lower()) - ord('a')] += 1.0
            else:
                strange_characters += 1
        
        if strange_characters >= len(text)//3:
            return 0
        
        return math.exp(-cls.likeliness(letter_frequency))
        
    
    