from collections import Counter


def identify(middle: int):
    s = 0
    for i in range(n):
        if a[i] < middle:
            s += middle - a[i]
    return s <= k


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    left = 1
    right = 2e12
    c = 0
    while left <= right:
        middle = (left + right) // 2
        if identify(middle):
            c = middle
            left = middle + 1
        else:
            right = middle - 1
    cnt = 0
    for i in range(n):
        if a[i] > c:
            cnt += 1
        else:
            k -= c - a[i]
    print(int(c * n - n + 1 + cnt + k))
