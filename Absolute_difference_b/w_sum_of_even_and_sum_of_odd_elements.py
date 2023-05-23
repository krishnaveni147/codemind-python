n = int(input())
lst = list(map(int, input().split()))
print(abs(sum(j for j in lst if j % 2 ==1) -sum(i for i in lst if i % 2 == 0)))