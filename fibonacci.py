n = int(input())
a = 0
b = 1
c = a + b
print(a, b, c, end = " ")
while n - 3:
    a = b
    b = c
    c = a + b
    print(c, end = " ")
    n -= 1
    