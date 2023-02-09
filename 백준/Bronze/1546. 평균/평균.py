N = int(input())
scores = list(map(int,input().split()))
max = max(scores)
sum = 0
for i in range(N):
    scores[i] = scores[i]/max*100
    sum += scores[i]
avg = sum / N
print(avg)