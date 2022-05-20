import math
def sieve():
    arr = [0]*(n+1)
    arr[0] = 1
    arr[1] = 1

    for i in  range(2,int(math.sqrt(n)+1)):
        if  arr[i] == 0:
            for j in range(i*i,n+1,i):
                arr[j] = 1
    rps = 0
    for i in range(1,n+1):
        if arr[i] == 0:
            rps += i
        dp[i] = rps
n = 1001
dp = [0]*(n+1)
l = int(input())
r = int(input())
sieve()
print(dp[r] - dp[l - 1])
