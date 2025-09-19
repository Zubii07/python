# Write a recursive function which to print all elements in a list(use list & index as parameter)

def print_list(lst, index):
    if(index == len(lst)):
        return
    print(lst[index])
    print_list(lst, index + 1)


fruits = ["apple", "banana", "cherry", "mango"]
print_list(fruits,0)
