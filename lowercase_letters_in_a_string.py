n = input()
count = 0
for i in range(0, len(n)):
    if n[i].islower():
        count += 1
print(count)