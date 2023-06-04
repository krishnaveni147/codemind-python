def hpy(n):
    x = n
    sum = 0
    while x > 0:
        c = x % 10
        sum = (sum + (c * c))
        x //= 10
    return sum
n = int(input())
hpy(n)
s = n
while s > 9:
    s = hpy(s)
if s == 1 or s == 7:
    print(True)
else:
    print(False)