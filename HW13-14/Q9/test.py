
from .question import Question

class Test:
    
    
    def __init__(self,
                 questions: Question,
                 count: int) -> None:
        
        self.questions = questions
        self.count = count
        
    
    def take_bank_file(self,
                       file: str) -> None:
        
        with open(file, "r") as f:
            f.read
        
        
        