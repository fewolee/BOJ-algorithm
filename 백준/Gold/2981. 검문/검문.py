from math import gcd
from math import sqrt
N = int(input())
num = []
M = []
for _ in range(N):
    num.append(int(input()))
num.sort()
temp = [num[i]-num[i-1] for i in range(1,N)]
my_gcd = temp[0]
for i in range(1,len(temp)):
    my_gcd = gcd(my_gcd,temp[i])
for i in range(2,int(sqrt(my_gcd)+1)):
    if my_gcd % i ==0:
        M.append(i)
        M.append(my_gcd//i)
M.append(my_gcd)
M = list(set(M))
M.sort()
for i in M:
    print(i, end=' ')
