import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    [a,b]= map(int,input().split())
    array.append([b,a])
array.sort()
for arr in array:
    tmp = arr[0]
    arr[0] = arr[1]
    arr[1] = tmp
for i in range(N):
    print(array[i][0], array[i][1])
