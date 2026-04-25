class Bank():
    def __init__ (self,amount):
        self.amount=amount
    def check_balance(self):
        print("your balance is:",self.amount)
    def add_amount(self,value):
        self.amount+=value
        print(f"{value} added-final amount:{self.amount}")
    def withdraw_amount(self,value):
        if value>self.amount:
            print("insufficient")
        else:
            self.amount-=value
            print(value)


obj1=Bank(5000)
obj1.add_amount(1000)
obj1.withdraw_amount(3000)

