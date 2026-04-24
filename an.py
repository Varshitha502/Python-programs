class dog():
    def __init__(self,name,breed):
        self.a=name
        self.b=breed
        print(f"{self.a}is born!")
    def bark(self):
          print(f"name:{self.a}")
          print("woff!!") 
    def fetch(self,object):
          print(f"got{object}")
my_dog1=dog("max","pug")
my_dog1.bark()