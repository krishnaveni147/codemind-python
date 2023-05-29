l = list(map(str, input().split()))
d = []
for i in l:
    c = 0
    for j in i:
        if j in "aeiouAEIOU":
            c += 1
    d.append(c)
dup = []
for i in d:
    if i == min(d):
        dup.append(i)
print(len(dup))