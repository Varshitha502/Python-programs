class Cls1():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("a:",a)
        print("b:",b)
class Cls2():
    def __init__(self,c,d):
        self.c=c
        self.d=d
        print("c:",c)
        print("d:",d)
class child(Cls1,Cls2):
    def __init__(self,a,b,c,d):
        Cls1.__init__(self,d,b)
        Cls2.__init__(self,c,a)
    def hello():
        print("hi")
obj1=child(3,5,6,7)