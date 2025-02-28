# Program to count number of digits in a number. e.g: 12345=> digits are 5
N = int(input("Enter an integer: "))

count = 0

# Handle the case when N is 0
if N == 0:
    count = 1
else:
    while N > 0:
        N //= 10  # Remove the last digit
        count += 1  
print("Number of digits:", count)
