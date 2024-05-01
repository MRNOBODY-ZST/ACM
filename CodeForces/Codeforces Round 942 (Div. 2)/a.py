t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for j in range(n):
        if a[j] > b[j]:
            a.insert(j, b[j])
            a.pop(-1)
            cnt += 1
    print(cnt)
        