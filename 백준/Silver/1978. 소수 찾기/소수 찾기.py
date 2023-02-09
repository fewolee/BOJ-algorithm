N = int(input())
prime = 0
n_list = list(map(int,input().split()))
for n in n_list:
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if count ==1:
        pass
    elif count <= 2:
        prime += 1
print(prime)