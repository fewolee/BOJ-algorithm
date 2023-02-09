N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
arr.sort()
for i in arr:
    print(i)