text = input("Enter a text to check if palindrom or not: ")
if text == text[::-1]:
    print("Palindrom")
else:
    print("Not a palindrom")
