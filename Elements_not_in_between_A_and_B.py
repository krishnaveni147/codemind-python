n = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())
k = 0
for i in l:
    if(i < a or i > b):
        print(i, end = ' ')
        k += 1
if k == 0:
    print(-1)