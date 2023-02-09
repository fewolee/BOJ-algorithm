n_list= list()
for _ in range(9):
    n = int(input())
    n_list.append(n)
max = max(n_list)
print(max)
print(n_list.index(max)+1)