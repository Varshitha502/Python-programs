num=int(input("enter number:"))
p=1
while num>0:
    p=p*num%10
    num=num//10
    print(p)
