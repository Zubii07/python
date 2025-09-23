# Create account class with 2 attributes(balance & account No.) 
# and create methods for debit, credit & printing the balance.


class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}")
            print(f"Total balance is: {self.get_balance()}")
    
    def credit(self,amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}")
        print(f"Total balance is: {self.get_balance()}")
    
    def get_balance(self):
        return self.balance

acc1 = Account(1000, "001234")
acc1.debit(200)
acc1.credit(500)
