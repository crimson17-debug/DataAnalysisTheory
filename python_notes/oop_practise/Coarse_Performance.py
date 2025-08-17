class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age


class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id


class  Course:
    def __init__(self,name,teacher,students,grades):
        self.name = name
        self.teacher = teacher
        self.students = students
        self.grades = grades

        