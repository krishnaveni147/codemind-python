n = int(input())
arr = list(map(int, input().split()))
l=[]
k = []
c = 0
sum = 0
x, y = map(int, input().split())
for i in range(x, y+1):
    l.append(i)
for i in arr:
    if i not in l:
        k.append(i)
        c += 1
if c > 0:
    print(max(k))
else:
    print(-1)
    
    