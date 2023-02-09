N = int(input())
P = list(map(int,input().split()))
P.sort()
time = []
sum = 0
for i in P:
    sum +=i
    time.append(sum)
last = 0
for j in time:
    last += j
print(last)