# Make a class of programmers which are working in Microsoft.

class programmers:
    company = 'Microsoft'
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary

p = programmers('Zohaib','Web Developer', 12344)
print(p.name,p.role,p.salary,p.company)        