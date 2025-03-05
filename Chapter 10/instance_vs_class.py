
class Employee:    # This is class Attribute
    name = 'Ali'
    language = 'C'
    sallary = 12333

data = Employee()
data.language = 'Python'    # This is an instance attribute
print(data.name,data.language)  # Instance object take prefernece over class attributes during assignment & retrival