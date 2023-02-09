N, K = map(int,input().split())
value = []
for _ in range(N):
    value.append(int(input()))
cnt = 0
value = value[::-1]
for cost in value:
    cnt = cnt + K//cost
    K = K % cost
    if K ==0:
        break
print(cnt)

