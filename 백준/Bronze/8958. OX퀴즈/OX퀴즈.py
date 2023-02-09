N = int(input())
for _ in range(N):
    arr = list(map(str,input()))
    num = 0
    scores = []
    for i in arr:
        if(i=='O'):
            num+=1
            scores.append(num)
        else:
            num = 0
            scores.append(num)
    print(sum(scores))