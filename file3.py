try:
    with open("file4.txt","r") as e:
      data=e.read()
    print(data)  
except FileNotFoundError:
     print("error! file not found")