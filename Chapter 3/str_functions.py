 # len(): this function returns the length of the string.e.g
name = "Zohaib"
print(len(name))  # Output: 6

### **1. String Manipulation**
str.upper()    #  Converts all characters to uppercase.
str.lower()    #  Converts all characters to lowercase.
str.title()    #  Converts the first letter of each word to uppercase.
str.capitalize() # Capitalizes the first letter of the string.
str.swapcase() # Swaps uppercase letters to lowercase and vice versa.
str.strip()   # Removes leading and trailing whitespaces.
str.lstrip() # Removes leading whitespaces.
str.rstrip() # Removes trailing whitespaces.

### **2. Searching and Replacing**
str.find()  # Returns the index of the first occurrence of a substring, or `-1` if not found.
str.index() #  Similar to `find()`, but raises an exception if not found.
str.rfind()  # Returns the last occurrence of a substring.
str.replace() # Replaces occurrences of `old` with `new`.
str.count()   # Counts occurrences of a substring.

### **3. Checking String Properties**
str.startswith()  #  Checks if a string starts with the given substring.
str.endswith()   # Checks if a string ends with the given substring.
str.isalpha() #  Checks if all characters are alphabetic.
str.isdigit() #  Checks if all characters are digits.
str.isalnum() #  Checks if all characters are alphanumeric.
str.isspace() #  Checks if the string contains only whitespace.
str.islower() #  Checks if all characters are lowercase.
str.isupper() #  Checks if all characters are uppercase.
str.istitle() #  Checks if the string follows title case.

### **4. String Splitting and Joining**
str.split()  #  Splits the string into a list based on a separator.
str.rsplit()  # Splits from the right.
str.splitlines()   # Splits the string by line breaks.
str.join()  #  Joins elements of an iterable into a string.

### **5. Formatting Strings**
str.center( ) #  Centers the string with padding.
str.ljust()  # Left-justifies the string.
str.rjust()  # Right-justifies the string.
str.zfill()   # Pads the string with leading zeros.
str.format()   # Formats the string with placeholders.


### **6. Encoding and Decoding**
str.encode(encoding="utf-8")   #  Encodes the string into bytes.
bytes.decode(encoding="utf-8") #  Decodes bytes back into a string.

### **7. String Translation**
str.maketrans(dict)   # Creates a translation table.
str.translate()  #  Replaces characters using the translation table.
