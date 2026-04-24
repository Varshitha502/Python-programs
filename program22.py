s="ABC"
for i in s:
    for j in s:
        for k in s:
            if i!=j and j!=k and i!=k:
                print(i+j+k)