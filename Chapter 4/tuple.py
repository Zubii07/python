# tuple is an immutable data type in Python.



# Creating a tuple
my_tuple = (1, 2, 3, "hello", True)

# Accessing elements
print(my_tuple[0])   # Output: 1
print(my_tuple[3])   # Output: "hello"

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, d)  # Output: 1 hello

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, "hello")

# Attempting to modify a tuple (will raise an error)
# my_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment
