
class Student:
    def __init__(self, name, age, average_mark):
        self.name = name
        self.age = age
        self.average_mark = average_mark

    def change_average_mark(self, new_average_mark):
        self.average_mark = new_average_mark

    def student_info(self):
        print(f'Name: {self.name}, Age: {self.age} Average mark: {self.average_mark}')

student_data = Student("Tom", 18, 33.7)
student_data.student_info()
student_data.change_average_mark(40)
student_data.student_info()