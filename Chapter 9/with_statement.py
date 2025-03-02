f = open("file.txt")
data = f.read()
print(data)
f.close() 


# The same can be written using with statement like this:
with open("myFile.txt") as f:
    print(f.read())


# you don't have to explicitly close the file    