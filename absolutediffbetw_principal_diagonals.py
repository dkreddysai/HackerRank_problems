arr=[[1,2,3],
     [4,5,6],
     [9,8,9]]
n=len(arr)
# Hacker rank
def absdiff_pdiagonals(arr):
    LTOR = 0
    RTOL = 0
    for i in range(0,n):
        LTOR+=arr[i][i]
        RTOL+=arr[i][n-1-i]
        a=abs(LTOR-RTOL)
    return a
print(absdiff_pdiagonals(arr))