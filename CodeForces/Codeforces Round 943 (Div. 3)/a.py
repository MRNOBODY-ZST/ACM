t = int(input())
from math import gcd

for _ in range(t):
    max_num = 0
    max_y = 0
    x = int(input())
    for i in range(1, x):
        gcd_num = gcd(i, x)
        if gcd_num + i > max_num:
            max_num = gcd_num + i
            max_y = i
    print(max_y)

