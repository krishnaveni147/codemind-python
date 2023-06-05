def prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return 0
    return 1
    
a = int(input())
b = int(input())
s = a + b
s1 = a + b +1
while prime(s1) == False:
    s1 += 1
print(s1 - s)
