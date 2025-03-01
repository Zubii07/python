# Program to print the following patterns:
'''
***
**
*
'''


# By using recursion

def pattern(n):
    if(n==0):
        return
    print('*' * n)
    pattern(n-1)


pattern(3)    