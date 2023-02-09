H, M = map(int, input().split())
count = 0
if(M<45 and H>0):
    H-=1
    M+=15
elif(M<45 and H==0):
    H+=23
    M+=15
else :
    M-=45
print(H, M)
