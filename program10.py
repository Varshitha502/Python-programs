str=input("enter any string:")
for ch in str:
    if str.count(ch)==1:
        print(ch)
        break
    else:
        print("No non-repeating character found")