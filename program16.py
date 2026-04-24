str1="cat"
str2="cut"
diff=0
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        diff+=1
print(len(str1)==len(str2)and diff==1)
