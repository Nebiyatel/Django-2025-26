class Student:
    def __init__(self):
        self.__grade = 0

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

student1 = Student()
student1.set_grade(85)
print(student1.get_grade())
