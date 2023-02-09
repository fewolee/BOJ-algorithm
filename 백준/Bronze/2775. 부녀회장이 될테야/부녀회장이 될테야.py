T = int(input())
for _ in range(T):
    floor = int(input()) #층
    num = int(input()) #호
    f0 = [x for x in range(1,num+1)] #0층
    for k in range(floor): # 층 수만큼 반복
            for i in range(1,num):
                f0[i] += f0[i-1]
    print(f0[-1])
