arr=[1,1,0,-1,-1]
def plusMinus(arr):
    # Write your code here
    n=len(arr)
    a=0
    b=0
    x=0
    for i in arr:
        if(i>0):
            a+=1
        elif(i<0):
            b+=1
        elif(i==0):
            x+=1
    c=f"{a/n:.6f}"
    d=f"{b/n:.6f}"
    e=f"{x/n:.6f}"
    print(c)
    print(d)
    print(e)

plusMinus(arr)