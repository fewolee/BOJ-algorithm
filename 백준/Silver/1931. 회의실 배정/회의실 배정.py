N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int,input().split())
    meeting.append([start,end])
meeting = sorted(meeting,key = lambda a: a[0])
meeting = sorted(meeting,key = lambda a: a[1])
last = 0
cnt = 0
for i,j in meeting:
    if i >= last:
        cnt+=1
        last = j
print(cnt)