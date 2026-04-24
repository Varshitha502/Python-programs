list=[1,2,3,4]
if list==sorted(list) or list==sorted(list,reverse=True):
    print("monotonic")
else:
    print("no monotonic")