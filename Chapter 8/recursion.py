# Recursion is a function which calls itself.
# For example to find the factorial of any number , we use the formula:
# factorial(n) = n * factorial(n-1)


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input('Enter a num:'))
print(f" The factorial of this number is: {factorial(n)}")



# Write a recursive function which calculate the sum of first n natural numbers.
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

n = int(input('Enter a num:'))
print(f"The sum of first {n} natural numbers is: {calc_sum(n)}")

