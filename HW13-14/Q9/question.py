
class Question:
    
    def __init__(self,
                 question_text: str,
                 option1: str,
                 option2: str,
                 option3: str,
                 option4: str,
                 correct_answer: str) -> None:
        
        self._question_text = question_text
        self._option1 = option1
        self._option2 = option2
        self._option3 = option3
        self._option4 = option4
        self._correct_answer = correct_answer
        
    @property 
    def question_text(self) -> str:
        return self._question_text
    
    @property
    def option1(self) -> str:
        return self._option1
    
    @property
    def option2(self) -> str:
        return self._option2
    
    @property
    def option3(self) -> str:
        return self._option3
    
    @property
    def option4(self) -> str:
        return self._option4
    
    @property
    def correct_answer(self) -> str:
        return self._correct_answer