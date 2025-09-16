#WAP to check list is palindrom of not

list1 = [1,2,1]
copy_list = list1.copy() # return a shallow copy of list1
copy_list.reverse() # reverse the copy_list
if list1 == copy_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
