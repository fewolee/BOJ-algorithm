import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dict = {}
for i in range(1,N+1):
    dict[i] = i
for _ in range(M):
    i, j = map(int,input().split())
    tmp = dict[i]
    dict[i] = dict[j]
    dict[j] = tmp
for i in range(1,N+1):
    print(dict[i],end=" ")
