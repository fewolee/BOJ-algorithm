def fact(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result
N, K = map(int,input().split())
print(int(fact(N) / fact(K) / fact(N-K)))