str=input("enter any string:")
vowels=0
consonants=0
for ch in str:
        if ch in 'aeiouAEIOU':
            vowels+=1
        else:
            consonants+=1
print("Vowels:", vowels)
print("Consonants:", consonants)