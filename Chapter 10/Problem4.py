# Write a class train which has method to book a ticket, get Status and get fare information of train
from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo
        pass
    def book(self,fro,to):
        print(f" Ticket is booked in train NO: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f" Train No: {self.trainNo} is running on time")

    def fare(self,fro,to):
        print(f" Ticket fare in train NO: {self.trainNo} from {fro} to {to} is {randint(22,555)}")

t = Train(122)
t.book('Karachi', 'Lahore')
t.getStatus()
t.fare('Karachi', 'Lahore')