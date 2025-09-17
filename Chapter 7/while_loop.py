# In while loop, condition executes first.
# Example: Print the contents of list using While loop:

list = ['Introduction','Daffodils', 'Try Again','Three Days to See']

i = 0

while(i<len(list)):
    print(list[i])
    i+=1



# Print counting from 1 to 50

counting = 1

while(counting<51):
    print(counting)
    counting+=1


# Print table
number = int(input("Enter a number to print its table:"))
i = 1
while(i<=10):
    print(number, "x", i, "=", number*i)
    i+=1
