class Mat1():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class Mat2(Mat1): 
    def mul(slef,a,b):
        return a*b
obj1=Mat2()
ans=obj1.add(3,4)
print(ans)
