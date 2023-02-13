from math import factorial
n = int(input())
factnum = factorial(n)
strs = str(factnum)[::-1]
cnt = 0
for i in strs:
    if i != '0':
        break
    cnt +=1
print(cnt)