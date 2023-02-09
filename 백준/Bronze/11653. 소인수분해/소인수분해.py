import sys
N = int(input())
if(N==1):
    sys.exit()
for i in range(2,N+1):
    if N%i==0:
        while N%i ==0:
            print(i)
            N=N/i
