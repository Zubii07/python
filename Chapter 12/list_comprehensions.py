myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# This can be done using list_comprehensions like this:
squaredList = [i*i for i in myList]

print(squaredList)