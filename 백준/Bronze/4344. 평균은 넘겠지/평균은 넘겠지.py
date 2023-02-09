C = int(input())
for _ in range(C):
    arr = list(map(int,input().split()))
    student = arr[0]
    arr= arr[1:]
    avg = sum(arr) / student
    num = 0
    for i in arr:
        if(i>avg):
            num +=1
    rate = num / student * 100
    print(f"{rate:.3f}%")