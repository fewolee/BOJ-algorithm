N = int(input())
money = [500,100,50,10,5,1]
M = 1000-N # 거스름돈
cnt = 0
for num in money:
    cnt+= M//num
    M = M % num
print(cnt)
    