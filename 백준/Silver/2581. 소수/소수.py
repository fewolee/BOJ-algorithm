M = int(input())
N = int(input())
prime_list = []
def prime(n):
    cnt = 0
    if n<2:
        return False
    else:
        for i in range(1,n+1):
            if(n%i==0):
                cnt+=1
        if cnt<=2:
            return True
        else:
            return False
for n in range(M,N+1):
    if(prime(n) == True):
        prime_list.append(n)
if(len(prime_list)<1):
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))