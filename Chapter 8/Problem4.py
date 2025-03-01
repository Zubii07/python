# function to convert inch to cm:

def inch_to_cm(inch):
    return inch * 2.54

n = int(input(' Enter value in Inch: '))
print(f"The value in cm is: {inch_to_cm(n)}")