N, M = map(int,input().split())
s1 = set()
s2 = set()
for _ in range(N):
    s1.add(input())
for _ in range(M):
    s2.add(input())
result = sorted(list(s1 & s2))
print(len(result))
for i in result:
    print(i)
