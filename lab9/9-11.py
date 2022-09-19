class Student:
    def __init__(self, name, st_id, kor=0, math=0, sci=0, tot=0):
        self.__name = name
        self.__student_id = st_id
        self.__korean_quiz = kor
        self.__math_quiz = math
        self.__science_quiz = sci
        self.__tot_quiz = tot

    def __str__(self):
        return '이름 : {}, 학번 : {}\n국어성적 : {}, 수학성적 : {}, 과학성적 : {}\n합계 : {}, 평균 : {:.1f}'.format(self.__name, self.__student_id, self.__korean_quiz,
                                                                                            self.__math_quiz, self.__science_quiz, self.get_total_score(), self.get_avg_score())
                                                    
    def set_korean_quiz(self, kor):
        self.__korean_quiz = kor

    def set_math_quiz(self, math):
        self.__math_quiz = math

    def set_science_quiz(self, sci):
        self.__science_quiz = sci

    def get_korean_quiz(self):
        return self.__korean_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def get_science_quiz(self):
        return self.__science_quiz
    
    def get_total_score(self):
        self.__tot_quiz = self.get_korean_quiz() + self.get_math_quiz() + self.get_science_quiz()
        return self.__tot_quiz

    def get_avg_score(self):
        avg = self.get_total_score()/3
        return avg
    
name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')

student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)
