
class Employee:    # This is class Attribute
    name = 'Ali'
    language = 'C'
    salary = 12333

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print('I am creating an object')  # dunder method which is automatically called


    def getinfo(self):
        print(f"The language is {self.language} and Salary is {self.salary}")    

data = Employee('Zohaib', 'Python', 120000)
# data.college = 'LIST'    # This is an instance attribute
print(data.name,data.language, data.salary)

# Whenever we created an object, the init(dunder method) is automatically called.e.g:
# Ali = Employee()  