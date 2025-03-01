# function to convert celcius to fahrenheit

def f_to_c(f):
    return 5*(f-32)/9

f = int(input('Enter a temperature in fahrenheit: '))
result = f_to_c(f)

print(f"Temperature in celsius is: {round(result,2)}°C")