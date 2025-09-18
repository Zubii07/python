#Given a list ["apple", "banana", "cherry"], use a for loop to print each element with its index.


fruits = ["apple", "banana", "cherry"]
index = 0
for fruit in fruits:
    print(f'Index {index}: {fruit}')
    index += 1


# Write a for loop to count the number of vowels in a string.
string = "Hello World"
count = 0
for char in string.lower():
    if char in 'aeiou':
        count += 1
print(f"Total number of vowels in {string}: {count}")





#Write a program that prints all even numbers between 1 and 50 using a for loop.

for num in range(1,51):
    if num%2 == 0:
        print(num)



# Write a for loop to reverse a string (without using slicing).
string = "Hello"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"reversed string of  {string}: {reversed_string}")
