K = int(input())
height = []
width = []
total = []
for _ in range(6):
    dir, length = map(int,input().split())
    if dir==1 or dir ==2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)
big_square = max(height) * max(width)
max_hindex = total.index(max(height))
max_windex = total.index(max(width))
small_width = abs(total[max_hindex-1]-total[(max_hindex-5 if max_hindex==5 else max_hindex+1)])
small_height = abs(total[max_windex-1]-total[(max_windex-5 if max_windex==5 else max_windex+1)])
area = big_square -  (small_width * small_height)
print(area*K)
