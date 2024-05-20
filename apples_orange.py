s=7
t=10
a=4
b=12
m=3
n=3
apples=[2,3,-4]
oranges=[3,-2,-4]
fcount=0
ocount=0
for i in apples:
    fapple=i+a
    if (s <= fapple <= t):
        fcount+=1
for j in oranges:
    forange=j+b
    if (s <= forange <=t):
        ocount+=1
print(fcount)
print(ocount)