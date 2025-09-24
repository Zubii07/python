

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

C1 = Circle(5)
print(f"Area of circle with radius {C1.radius} is: {C1.area()}")
print(f"Perimeter of circle with radius {C1.radius} is: {C1.perimeter()}")
