t = int(input())

for _ in range(t):
    n, k, pb, ps = map(int, input().split())
    pb -= 1
    ps -= 1
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b_sum, s_sum = 0, 0

    cur = 0
    for i in range(min(k, n + 1)):
        cur += a[pb]
        b_sum = max(b_sum, cur + a[pb] * (k - i - 1))
        pb = p[pb] - 1

    cur = 0
    for i in range(min(k, n + 1)):
        cur += a[ps]
        s_sum = max(s_sum, cur + a[ps] * (k - i - 1))
        ps = p[ps] - 1

    if s_sum == b_sum:
        print("Draw")
    elif b_sum > s_sum:
        print("Bodya")
    else:
        print("Sasha")