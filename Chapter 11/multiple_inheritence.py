class Employee:
    company = 'Sygnls'
    name = 'default name'
    def show(self):
        print(f" The name of employee is {self.name} and the company is {self.company}")



class coder:
    language = 'Python'
    def printlanguage(self):
        print(f" Out of all the languages, here is your language: {self.language}")


class programmer(Employee,coder):
    company = 'Softminds'
    def showlanguage(self):
        print(f" The name is {self.company} and he is good with {self.language} language")



a = Employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()