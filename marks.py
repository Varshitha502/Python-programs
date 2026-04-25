student_records=[
    ('alice',{'math':92,'science':88}),
    ('bob',{'math':85,'science':95}),
    ('charlie',{'math':78,'science':82})
]
for name,subject in student_records:
    for marks in subject:
        if subject[marks]>=90:
            print(name,marks)


    