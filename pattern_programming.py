print("METHOD-1")
n=5
for i in range(0,n):
    #print("*")
    print("*",end=" ")
print()


print("METHOD-2")
n=7
for i in range(0,n):
    for j in range(0,n): # print 5 stars in a row
        print("*",end=" ")
    print() #take cursor to a new line


print("METHOD-3")
n=5
for i in range(0,n):
    for j in range(0,n):
        print(i+1,end=" ") # All rows have same numbers..
    print()


print("METHOD-4")
n=5
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ") # All columns have same numbers..
    print()

print("METHOD-5__Rectangle type pattern:")
n=5
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==n-1 or j==0 or j==n-1): # two rows that is first row[i=0] and last row[n-1] are stars and also 2 columns thar is first column and last column are stars..remaining all are empty spaces
            print("*",end="")
        else:
            print(" ",end="")
    print()


print("METHOD-6")
n=5
count=1
for i in range(0,n):
    for j in range(0,n):
        if(count<10):
            print("0",end="")

        print(count,end=" ")
        count+=1
    print()