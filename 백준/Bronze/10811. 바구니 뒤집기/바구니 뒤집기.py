import sys
input = sys.stdin.readline
N,M = map(int,input().split())
basket = [i+1 for i in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    basket[a-1:b] = basket[a-1:b][::-1]

for i in range(N):
    print(basket[i],end=" ")
