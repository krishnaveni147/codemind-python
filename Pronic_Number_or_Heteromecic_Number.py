n = int(input())
f = 0
for i in range(n):
    if n == i*(i + 1):
        f = 1
        break
if f == 1:
    print("YES")
else:
    print("NO")