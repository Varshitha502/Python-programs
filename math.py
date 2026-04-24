class MathDemo:
    def __init__(self,amount):
        self.amount=amount
    def add_amount(self,value):
        self.amount+=value
        print(f"{value}added:final amount:{self.amount}")
    def remove_amount(self,value):
        self.amount-=value
        print(f"{value}removed:final amount:{self.amount}")
obj1=MathDemo(1000)
obj1.add_amount(500)
obj1.remove_amount(200)