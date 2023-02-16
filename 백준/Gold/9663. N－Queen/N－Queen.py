n = int(input())
row = [0] * n
res = 0
def promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def queen(x):
    global res
    if x==n:
        res +=1
        return
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                queen(x+1)

queen(0)
print(res)
