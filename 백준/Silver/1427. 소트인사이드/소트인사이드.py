N = int(input())
num = []
while N>0:
    num.append(N%10)
    N = N//10
num.sort()
num = num[::-1]
for i in num:
    print(i, end='')