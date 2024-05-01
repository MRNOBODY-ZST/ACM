t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    flag = 0
    for j in range(n):
        if j == p[p[j] - 1] - 1:
            flag = 1
            break
    if flag:
        print('2')
    else:
        print('3')