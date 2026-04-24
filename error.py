try:
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    c=a/b
    print(c)
except ValueError:
    print("this is value error")
except ZeroDivisionError:
    print("this is zero division erroe") 
except Exception as e:
    print(e)