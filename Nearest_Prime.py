
def prime(n):
    if (n == 1):
        return 0
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return 0
    return 1
for i in range(int(input())):
    n = int(input())
    c = 1
    t = n
    while(1):
        if(prime(n + c)):
            break
        c += 1
    while(n):
        if(prime(n)):
            break
        n -= 1
    if((t-n)<=c):
        print(n)
    elif(c<(t-n)):
        print(t + c)
        