from math import gcd
t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    i = gcd(a,b)
    cnt = b
    for j in range(a+b,0,-1):
        if j%i == 0:
            cnt += 1
    print(cnt)