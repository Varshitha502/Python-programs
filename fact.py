def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
factorial=fact(5)
print(factorial)