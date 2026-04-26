class Bank_Account():
    def __init__(self,ac_num,ac_name,balance):
        self.ac_num=ac_num
        self.ac_name=ac_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
    def check_balance(self):
        print("balance:",self.balance)
bank=Bank_Account(123456,"varshu",987654)
bank.deposit(12345)
bank.withdraw(9876)
bank.check_balance()