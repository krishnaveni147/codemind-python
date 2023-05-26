n = int(input())
a = list(map(int, input().split()))
c = []
for i in a:
    s=0
    if i<0:
        i*=-1
    if i==0:
        s=1
    while i:
        s+=1
        i//=10
    c.append(s)
print(*c)