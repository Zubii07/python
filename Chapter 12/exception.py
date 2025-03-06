# There are many buit-in exceptions which are raised in python when something goes wrong.
# Exception in python can be handled using a try statement. The code that handled the exception is written
# in the except clause.


try:
    # code that might throw exception
    a = int(input(' Enter a number: '))
    print(a)


except Exception as e:
    print(e)    


print('Thank you.')  # It will always print    