class UserAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def check_bal(self):
        print("balance:",self.balance)
    def deposit_amount(self,amount):
        self.balance+=amount
        print("deposite amount:",self.balance)
    def withdraw_amount(self,amount):
        self.balance-=amount
        print("withdraw amount:",self.balance)
user1=UserAccount("varsha",5000)
user1.check_bal()
user1.deposit_amount(1000)
user1.withdraw_amount(3000)

