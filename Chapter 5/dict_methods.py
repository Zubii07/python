# .items(): returns a list of (key,value)tuples. e.g:

Marks = {
    'Math': 90,
    'English': 80,
    'Science': 85
}

print(Marks.items())  # Output: dict_items([('Math', 90), ('English', 80), ('Science', 85)])

# .keys(): returns a list of dictionary keys. e.g:
print(Marks.keys())  # Output: dict_keys(['Math', 'English', 'Science'])

# .values(): returns a list of dictionary values. e.g:
print(Marks.values())  # Output: dict_values([90, 80, 85])


# .update(): updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs. e.g:

Marks.update({'Math': 95, 'Urdu': 75})
print(Marks)  # Output: {'Math': 95, 'English': 80, 'Science': 85, 'Urdu': 75}


# .pop(): removes the item with the specified key name. e.g:
Marks.pop('Science')
print(Marks)  # Output: {'Math': 95, 'English': 80, 'Urdu': 75}
