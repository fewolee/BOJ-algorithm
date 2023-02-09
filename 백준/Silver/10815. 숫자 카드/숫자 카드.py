import sys
input = sys.stdin.readline
N = int(input())
card = []
test = []
card = list(map(int,input().split()))
M = int(input())
test = list(map(int,input().split()))

dict = {}
for i in range(N):
    dict[card[i]] = 0
for j in range(M):
    if test[j] in dict:
        print(1,end=' ')
    else:
        print(0,end =' ')
