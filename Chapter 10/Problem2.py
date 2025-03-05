# Write a class 'Calculator' capable of finding square,cube and square root of a number.


class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square is {self.num*self.num}")    

    def cube(self):
        print(f"cube is {self.num*self.num*self.num}") 

    def squareroot(self):
        print(f"Square Root is {self.num**1/2}") 

a = Calculator(4)        
a.square()
a.cube()
a.squareroot()