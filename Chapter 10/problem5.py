# create student class that takes name & marks of 3 subject as arguments in constructor. 
# Then create a method to print the avg.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
    

student1 = Student("ALi", 85, 90, 78)
print(f"The average marks of {student1.name} is: {student1.avg()}")
