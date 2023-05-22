n = int(input())
sum = 0
sqrt = n * n
while (sqrt > 0):
    r = sqrt %10
    sum = sum + r
    sqrt = sqrt // 10
if (sum == n):
    print("Neon Number")
else:
    print("Not Neon Number")
