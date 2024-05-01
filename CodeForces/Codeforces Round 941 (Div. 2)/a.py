from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = Counter(c)
    if max(list(d.values())) < k:
        print(n)
    else:
        print(k - 1)
