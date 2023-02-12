from math import gcd
n = int(input())
ring = list(map(int,input().split()))
first = ring[0]
for i in range(1,n):
    if first % ring[i] == 0:
        print(f"{first//ring[i]}/{1}")
    else:
        my_gcd = gcd(first,ring[i])
        print(f"{first//my_gcd}/{ring[i]//my_gcd}")