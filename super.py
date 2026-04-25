class C():
      def __init__(self,a,b,c):
            self.a=a
            self._b=b
            self.__c=c
obj=C(10,20,30)
print(obj.a)
print(obj._b)
try:
      print(obj.__c)
except Exception:
      print("cant access in this way")
print(obj._C__c)