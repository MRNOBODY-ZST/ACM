cnt = 0
for i in range(0,pow(2,22)):
    if '1111111111' in bin(i):
        pass
    else:
        cnt+=1
print(cnt)