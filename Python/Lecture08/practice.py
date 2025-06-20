class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for var in self.marks:
            sum += var
        print("Hi", self.name, "Your Avg marks is: ", sum/3)

s1 = Student("Vaibhav", [99,98,97])

s1.get_avg()