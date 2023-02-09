import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int,input().split()))
array2 = sorted(list(set(array)))
dic = {}
for i in range(len(array2)):
    dic[array2[i]] = i
for i in array:
    print(dic[i],end=' ')