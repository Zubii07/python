# Program to read the text from the given file 'poem.txt' and find that whether it contains the word twinkle.


f = open('poem.txt')
content = f.read()
if("twinkle" in content):
    print('The word twinkle is present in the content')

else:
    print('The word twinkle is not present in the content')

f.close()    
