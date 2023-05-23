n = int(input())
lst = list(map(int, input().split()))
avg = sum(lst) // n 
if avg in lst:
    print("True")
else:
    print("False")