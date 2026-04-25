class fat():
    def father_method(self):
        print("hello")
class mot():
    def mother_method(self):
        print("hello")
class child(fat,mot):
    def child_method(self):
        print("hello c")
obj1=child()
a=obj1.child_method ()