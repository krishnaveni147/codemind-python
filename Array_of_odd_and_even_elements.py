n = int(input())
l = list(map(int, input().split()))
k = []
s = []
for i in l:
    if i % 2 != 0:
        k.append(i)
for i in l:
    if i % 2 == 0:
        s.append(i)
print(*(k + s))