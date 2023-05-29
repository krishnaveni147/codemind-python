string=input()
spcl_count=0
for i in range(0,len(string)):
    if (string[i].isalpha()):
        continue
    elif(string[i].isdigit()):
        continue
    elif(string[i]==' '):
        continue
    spcl_count+=1
print(spcl_count)