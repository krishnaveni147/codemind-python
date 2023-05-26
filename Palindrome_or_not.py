def ispalin(s):
    return s == s[::-1]
s = input()
s = s.lower()
result = ispalin(s)
if result:
    print("True")
else:
    print("False")