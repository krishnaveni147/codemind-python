n = int(input())
lst = list(map(int, input().split()))
print(abs(sum(lst[1::2]) + sum(lst[::2])))