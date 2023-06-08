n = int(input())
l = list(map(int, input().split()))
c = 0
k = 0
for i in l:
    k += i
    avg=k//n
for i in l:
    if i >= avg:
        c += 1
print(c)