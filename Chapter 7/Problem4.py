# Program to find the sum of first n natural numbers using while loop.

n = int(input('Enter Number: '))
i = 1
sum = 0

while(i<=n):
    sum += i
    i += 1

print(sum)


# using for loop

n = int(input('Enter Number: '))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
