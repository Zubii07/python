# Class is a blueprint for creating objects.


class Employee:    # This is class Attribute
    name = 'Ali'
    language = 'C'
    sallary = 12333

data = Employee()
data.college = 'LIST'    # This is an instance attribute
print(data.college,data.name,data.language)