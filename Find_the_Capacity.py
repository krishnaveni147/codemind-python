s, t, b = map(int, input().split())
c = 2*s*t*b*512
k=c//1024
print(k, end = 'KB')