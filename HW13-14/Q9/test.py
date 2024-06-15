
import re
import random

from question import Question

class Test:
    
    
    def __init__(self,
                 count: int) -> None:
        
        self.questions = []
        self.count = count
        
    
    def __test__(self,
                file: str) -> None:
        question_pattern = re.compile(r"^Question: (.*)", re.MULTILINE)
        options_pattern = re.compile(r"Ans\d{1}:\s{1}([\S]+)", re.MULTILINE)
        correct_answer_pattern = re.compile(r"^CorrectAnswer: (\d)", re.MULTILINE)
        
        with open(file, "r") as f:
            text = f.read()
        
        questions_lst = question_pattern.findall(text)
        options_lst = options_pattern.findall(text)
        correct_answers_lst = correct_answer_pattern.findall(text)
        
        question_index = 0
        answer_index = 0
        options_index = 0
        
        for _ in range(self.count):
            
            self.questions.append(
                                Question(
                                        questions_lst[question_index],
                                        options_lst[options_index],
                                        options_lst[options_index + 1],
                                        options_lst[options_index + 2],
                                        options_lst[options_index + 3],
                                        correct_answers_lst[answer_index]
                                        )
                                )
            
            question_index += 1
            answer_index += 1
            options_index += 4
        
        
    def makeTest(self,
                 count: int,
                 out_file: str) -> None:
        sample_questions = random.sample(self.questions, k = count)
        self.questions = sample_questions
        export_path = "Q9/"+ str(out_file) + ".txt"
        
        with open(export_path, "w") as f:
            
            for question in sample_questions:
                f.write(
                    f'''{question.question_text}\n
1.{question.option1}\t 2.{question.option2}\t 3.{question.option3}\t 4.{question.option4}\n
\n'''
                        )
        

test = Test(20)