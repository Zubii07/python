# .append(): to add an element to the end of the list e.g
Fruits = ['apple', 'banana', 'cherry']
print(Fruits) # Output: ['apple', 'banana', 'cherry']
Fruits.append('orange') 
print(Fruits) # Output: ['apple', 'banana', 'cherry', 'orange']


# .sort(): to sort the list in ascending order e.g
count = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(count) # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]
count.sort()
print(count) # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]


# .reverse(): to reverse the list e.g
count = [3, 1, 4, 1, 5, 9, 2, 6, 5]
count.reverse()
print(count)


# .insert(): to insert an element at a specific index e.g
alpha = ['a', 'b', 'd', 'e']
alpha.insert(2, 'c') # insert 'c' at index 2
print(alpha) # Output: ['a', 'b', 'c', 'd', 'e']


# pop(): to remove an element from the list e.g
value = ['1', '2', '3', '4', '5','11']
value.pop() # remove the last element
print(value) # Output: ['1', '2', '3', '4', '5']


# .remove(): to remove a specific element from the list e.g
value = ['1', '2', '3', '4', '5','11']
value.remove('3') # remove '11' from the list
print(value) # Output: ['1', '2', '3', '4', '5']