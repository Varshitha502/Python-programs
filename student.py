class student():
    def __init__(self,name,roll_number,sub1,sub2,sub3):
        self.name=name
        self.roll_number=roll_number
        self.marks=[sub1,sub2,sub3]
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total()/3
    def display(self):
        print("Name:",self.name)
        print("Roll_Number:",self.roll_number)
        print("Total:",self.total())
        print("Average:",self.average())
stu=student("varshu",502,90,99,95)
stu.display()
        