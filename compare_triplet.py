a=[1,2,3]
b=[3,2,1]
def Comparetriplet(a,b):
    Alice = 0
    Bob = 0
    for i in range(0,3):
        if a[i]>b[i]:
            Alice+=1
        elif a[i]<b[i]:
            Bob+=1
    return([Alice,Bob])
print(Comparetriplet(a,b))
