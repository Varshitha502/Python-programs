class Employee():
    def __init__(self,salary):
        self.salary=salary

class Manager(Employee):
    def total_salary(self):
        return self.salary+2000
class Developer(Employee):
    def total_salary(self):
        return self.salary+1000
m=Manager(50000)
d=Developer(10000)
print("manager salary:",m.total_salary())
print("developer salary:",d.total_salary())