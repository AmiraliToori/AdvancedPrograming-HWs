
class Student:
    
    
    def __init__(self, name: str,
                 std_id: str,
                 birth_date: str,
                 lessons: list) -> None:
        self.name = name
        self.std_id = std_id
        self.birth_date = birth_date
        self.lessons = lessons
        
    def __str__(self) -> str:
        return f'''{self.name} student with {self.std_id} ID, Born in {self.birth_date} have these lessons: 
{[lesson.lesson_title for lesson in self.lessons]} '''
        
    def __repr__(self) -> str:
        return f'''type:{type(self).__name__},
Student Name:{self.name} ,
Student ID:{self.std_id} ,
BoD:{self.birth_date} ,
Lessons:{self.lessons} '''
    
    
    def calculate_average(self) -> float:
        total_credit = 0
        total_score = 0
        
        for lesson in self.lessons:
            if lesson.score_announcement_status is True:
                total_score += lesson.score * lesson.credit
                total_credit += lesson.credit
            
        return f"The average score of {self.name} is: {round(total_score / total_credit, 2)}"
    
    def print_scores(self) -> None:
        print("List of lessons which their scores not submitted:")
        for lesson in self.lessons:
            if lesson.score_announcement_status == False:
                print(f"Lesson Title: {lesson.lesson_title}, Credit: {lesson.credit}")
    
    
    def change_score(self, lesson_id, score) -> None:
        if score > 20 or score < 0:
            raise ValueError("The new score is not valid!")
        # elif len(lesson_id) != 6:
        #     raise ValueError("The entered lesson id is not valid!")
        
        for lesson in self.lessons:
            
            if lesson.lesson_id == lesson_id:
                
                if lesson.score_announcement_status == True:
                    lesson.score = score
                else:
                    lesson.score_announcement_status == True
                    lesson.score = score
                

    def drop_course(self, lesson_id) -> None:
        for lesson in self.lessons:
            if lesson.lesson_id == lesson_id:
                self.lessons.remove(lesson)
                break
        else:
            raise ValueError("The lesson_id is not exist or not in the list of the courses that student have.")

############################################################################################################################

class Lesson:
    
    def __init__(self,
                 lesson_title: str,
                 credit: int,
                 score: float,
                 score_announcement_status: bool,
                 lesson_id: int) -> None:
        
        self.lesson_title = lesson_title
        self.credit = credit
        self.score = score
        self.score_announcement_status = score_announcement_status
        self.lesson_id = lesson_id
    
    
    def __str__(self) -> str:
        return f'''Lesson {self.lesson_title} with {self.lesson_id} have {self.credit} credit(s), the score situation is
{self.score_announcement_status} and the score is {self.score}.'''
                
    def __repr__(self) -> str:
        return f'''{type(self).__name__},
Lesson ID: {self.lesson_id},
Lesson Title: {self.lesson_title},
Credits: {self.credit},
Score announcement status: {self.score_announcement_status},
Score: {self.score}.'''
        
        
    def submit_score(self, new_score: float) -> None:
        
        if new_score < 0 or new_score > 20:
            raise ValueError("The entered Score is not valid!")
        
        self.score = new_score
        if self.score_announcement_status is False:
            self.score_announcement_status = True
        
        
########################################################
if __name__ == "__main__":
    
    course_1 = Lesson("Data Structures",
                    3,
                    15.2,
                    True,
                    151213)

    course_2 = Lesson("Java Programming",
                    3,
                    9.99,
                    True,
                    151214)

    course_3 = Lesson("Professional Language",
                    2,
                    None,
                    False,
                    151215)

    amirali_toori = Student("Amirali Toori",
                            "4001311982",
                            "2003",
                            [course_1, course_2, course_3])

    # print(str(amirali_toori))
    # print(repr(amirali_toori))

    # print(str(course_1))
    # print(repr(course_1))

    # print(course_3.score)
    # course_3.submit_score(20)
    # print(course_3.score)

    # print(amirali_toori.calculate_average())
    # print(amirali_toori.change_score(151214, 20))
    # print(amirali_toori.calculate_average())

    print(amirali_toori.drop_course(151215))
    print(str(amirali_toori))