# Program to print the following patterns:
'''
   *
  ***
 *****
'''

n = int(input('Enter Number: '))
for i in range(1,n+1):
    print(" " *(n-i), end="")
    print("*"*(2*i-1),end="")
    print("")


# Program to print the following patterns:
'''
*
**
***
'''

n = int(input('Enter Number: '))
for i in range(1,n+1):
    print("*" * i, end="")
    print("")


# Program to print the following patterns:
'''
***
* *
***
'''
n = int(input('Enter Number: '))
for i in range(1,n+1):
    if(i==0 or i==n):
        print("*" * n, end="")
        
    else:
        print("*",end="")
        print(" " * (n-2), end="")  
        print("*",end="")
    print(" ")  