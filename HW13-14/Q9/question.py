
class Question:
    
    def __init__(self,
                 question_text: str,
                 option1: str,
                 option2: str,
                 option3: str,
                 option4: str,
                 correct_answer: str) -> None:
        
        self.question_text = question_text
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer