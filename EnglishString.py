class EnglishString:
    def __init__(self, content: str, illegal: bool = False) -> None:
        self.content = content
        self.illegal = illegal
    
    @classmethod
    def illegal_string(cls):
        return cls('', illegal=True)
    
    def __str__(self):
        assert not self.illegal
        return self.content
    
    def __iter__(self):
        assert not self.illegal
        return iter(self.content)