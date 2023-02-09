numbers = []
count = 0
for _ in range(10):
    n = int(input())
    n = n % 42
    if(n in numbers):
        continue
    numbers.append(n)
    count +=1
print(count)