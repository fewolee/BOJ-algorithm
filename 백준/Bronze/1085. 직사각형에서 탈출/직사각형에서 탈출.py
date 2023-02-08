x,y,w,h = map(int,input().split())
distance = [x,w-x,y,h-y]
print(min(distance))