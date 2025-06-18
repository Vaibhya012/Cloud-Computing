class Student:
    college_name = "Shiv Chhatrapti College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("Welcome,", self.name)

s1 = Student("Kiran", 84)
print(s1.name, s1.marks)

s2 = Student("Vaishu", 90)
print(s2.name, s2.marks)
print(s2.college_name)
s2.welcome()