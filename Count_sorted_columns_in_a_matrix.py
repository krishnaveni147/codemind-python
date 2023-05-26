n, m = map(int, input().split())
l = [list(map(int, input().split()))for i in range(n)]
c = 0
for j in range(m):
    d = []
    for i in range(n):
        d.append(l[i][j])
    if(d == sorted(d) or d[::-1]==sorted(d)):
        c += 1
print(c)