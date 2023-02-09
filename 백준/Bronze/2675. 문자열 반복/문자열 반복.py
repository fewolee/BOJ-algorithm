T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    num = int(R)
    for n in S:
        print(n*num,end='')
    print()
