# program to detect spam messages.

p1 = 'Make a lot of money'
p2 = 'You win a prize bond'
p3 = 'Buy now'
p4 = 'Subscribe this'

message = input('Enter your comment: ')

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print('This comment is a spam')

else:
    print('This comment is not a spam')    