class Person:
    def __init__(self, name, age, designation,gender):
        self.name = name
        self.age = age
        self.designation = designation
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")
        print(f"My designation is: {self.designation}")
        print(f"Gender :{self.gender}")


class Student(Person):
    def __init__(self, name, age, designation,gender, student_id):
        super().__init__(name, age, designation,gender)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, designation,gender, subject):
        super().__init__(name, age,designation, gender)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Creating objects
student1 = Student("Jigme", 20, "Student","male", "S001")
teacher1 = Teacher("Mr. Thinley", 35, "HOD","male", "Mathematics")

# Example usage
student1.introduce()  # Output: Hello, my name is Jigme , I am 20 years old.
student1.study()      # Output: Jigme is studying.

teacher1.introduce()  # Output: Hello, my name is Mr. Thinley, I am 35 years old.
teacher1.teach()      # Output: Mr. Thinley is teaching Mathematics.
