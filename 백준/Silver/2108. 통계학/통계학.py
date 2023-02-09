import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num.sort()
cnt = Counter(num).most_common(2)
print(f"{round(sum(num)/N)}")
print(num[N//2])
if N >1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(num)-min(num))
