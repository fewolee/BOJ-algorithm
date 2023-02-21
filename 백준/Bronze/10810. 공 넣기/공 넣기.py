import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dict = {}
for i in range(1,N+1):
    dict[i] = 0
for _ in range(M):
    i, j, k = map(int,input().split())
    for n in range(i,j+1):
        dict[n] = k
for i in range(1,N+1):
    print(dict[i],end=" ")





