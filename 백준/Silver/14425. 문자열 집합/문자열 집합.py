import sys
input = sys.stdin.readline
N, M = map(int,input().split())
S = []
check = []
for _ in range(N):
    S.append(input())
for _ in range(M):
    check.append(input())
cnt = 0
for i in check:
    if i in S:
        cnt+=1
print(cnt)
    