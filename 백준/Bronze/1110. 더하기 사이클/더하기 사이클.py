N = int(input())
cycle = 0
if(N<10): N*=10
temp = N
while True:
    count = N//10 + N%10
    N = (N%10) *10 + count % 10
    cycle +=1
    if(N==temp) : break
print(cycle)