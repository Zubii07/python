#  function to find the greatest number among 3 numbers:


def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    

a = int(input('Enter Num a: '))    
b = int(input('Enter Num b: '))    
c = int(input('Enter Num c: '))    
print(f"The greatest Number is: {greatest(a,b,c)}")