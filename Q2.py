x = int(input())
i = 0
y = 1
verif = False
if(x==0 or x==1):
    verif = True
while(x>=y and verif==False):
    temp = y
    y = i + y
    i = temp
    if(x==y):
        verif = True
if(verif == True):
    print("Pertence")
else:
    print("Não Pertence")