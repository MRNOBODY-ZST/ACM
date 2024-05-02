t = int(input())
from collections import Counter
for _ in range(t):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    begin = min(a)
    a_dict = Counter(a)
    b = [0 for _ in range(n*n)]
    for i in range(n):
        b[i*n] = begin + i*c
    for i in range(n):
        for j in range(n):
            b[i*n+j] = b[i*n] + j*d
    b_dict = Counter(b)
    if a_dict == b_dict:
        print("YES")
    else:
        print("NO")
