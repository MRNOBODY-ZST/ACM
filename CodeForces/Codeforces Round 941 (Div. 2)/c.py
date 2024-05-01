t = int(input())

for _ in range(t):
    n = input()
    a = list(set(map(int, input().split())))
    a.sort()
    cnt = 0
    for i in range(len(a)-1):
        if a[i]+1 == a[i+1]:
            cnt+=1
    if cnt%2 == 0:
        print('Alice')
    else:
        print('Bob')