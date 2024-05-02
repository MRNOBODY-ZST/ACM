t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    a = [0 for i in range(n)]
    a[0] = x[0] + 1
    for i in range(1, n - 1):
        cnt = 0
        while a[i] <= x[i]:
            cnt += 1
            a[i] = a[i - 1] * cnt + x[i - 1]
    a[-1] = x[-1] + a[-2]
    print(" ".join(map(str, a)))
