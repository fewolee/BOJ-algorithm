word = list(input())
num = 0
for w in word:
    if w in "ABC":
        weight = 3
    elif w in "DEF":
        weight = 4
    elif w in "GHI":
        weight = 5
    elif w in "JKL":
        weight = 6
    elif w in "MNO":
        weight = 7
    elif w in "PQRS":
        weight = 8
    elif w in "TUV":
        weight = 9
    elif w in "WXYZ":
        weight = 10
    num += weight
print(num)