# Add a static method in problem 2, to greet the user with hello


class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square is {self.num*self.num}")    

    def cube(self):
        print(f"cube is {self.num*self.num*self.num}") 

    def squareroot(self):
        print(f"Square Root is {self.num**1/2}") 

    @staticmethod # we don't need self
    def hello():
        print('Hello there!')    

a = Calculator(4)   
a.hello()     
a.square()
a.cube()
a.squareroot()