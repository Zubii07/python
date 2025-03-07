# Map Example:
# The map() function applies a given function to all items in an input_list.

# Syntax:
# map(function_to_apply, list_of_inputs)

# Example:
# Convert a list of integers into strings using map()
 
numbers = [1, 2, 3, 4, 5]
numbers = list(map(str, numbers))
print(numbers)  # Output: ['1', '2', '3', '4', '5']


# Filter Example:
# The filter() function filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# Syntax:
# filter(function, sequence)

# Example:
# Filter the list of numbers which are greater than 3 using filter()                                
numbers = [1, 2, 3, 4, 5]
numbers = list(filter(lambda x: x > 3, numbers))
print(numbers)  # Output: [4, 5]



# Reduce Example:
# The reduce() function is defined in the 'functools' module. Like the map() and filter() functions, the reduce() function receives two arguments, a function and an iterable. However, it doesn't return another iterable, instead, it returns a single value.

# Syntax:
# reduce(function, sequence)

# Example:
# Find the sum of numbers in a list using reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)

print(sum)  # Output: 15

# Note: The reduce() function is not available in Python 3.0 and 3.1. It was moved to the 'functools' module in Python 3.0. So, you need to import the 'functools' module to use this function.