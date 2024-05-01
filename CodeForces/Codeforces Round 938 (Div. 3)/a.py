n = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[2]>=tmp[1]*2:
        print(tmp[0]*tmp[1])
    else:
        print(tmp[0]%2*tmp[1]+tmp[0]//2*tmp[2])
