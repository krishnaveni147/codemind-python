n, m = map(int, input().split())
a = [list(map(int, input().split()))for i in range(n)]
sum = 0
for i in range(n):
    for j in range(m):
        if (i == 0):
            sum += a[i][j]
        elif (i == n -1):
            sum += a[i][j]
        elif (j == 0):
            sum += a[i][j]
        elif (j == m - 1):
            sum += a[i][j]
print(sum)