class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
        self.coarses = []

    def display_info(self):
        print("Student Info: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} ")
        print(f"Sudent ID: {self.student_id}")
        print(f"Subjects: {self.coarses}")

    def enroll(self,course_name):
        self.coarses.append(course_name)



class Teacher(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.subjects = []


    def display_info(self):
        print("Teacher Info: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} ")
        print(f"Teacher ID: {self.employee_id}")
        print(f"Subjects: {self.subjects}")   


    def assign_subject(self,subject_name):
        self.subjects.append(subject_name)


# Create student
student1 = Student("Navya", 18, "CSE1001")
student1.enroll("Python")
student1.enroll("Math")

# Create teacher
teacher1 = Teacher("Priya", 32, "T102")
teacher1.assign_subject("Data Structures")
teacher1.assign_subject("Algorithms")

# Display info
student1.display_info()
teacher1.display_info()
