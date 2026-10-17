student = []
stnum = 3
subnum = 3
for st in range (stnum):
    stdata=[]
    name = input("you name :")
    stdata.append(name)
    for sub in range (subnum):
        s = input("enter degree")
        stdata.append(s)
    student.append(stdata)
    print(student)
