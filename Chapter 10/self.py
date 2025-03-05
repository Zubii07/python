# In object-oriented programming, whenever we define methods for a class, we use self as the 
# first parameter in each case. Let's look at the definition of a class called Cat.

class Cat:
    def Employee(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")
