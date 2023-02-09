N, X = map(int,input().split())
a_list = list(map(int,input().split()))
a = list()
for i in a_list:
    if(i<X):
        a.append(i)

for i in a:
    print(i,end=" ")