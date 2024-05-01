t = int(input())

from collections import Counter

for i in range(t):
    n = int(input())
    coin_list = input()
    coin_count = Counter(coin_list)
    if coin_count['U']%2 == 0:
        print('No')
    else:
        print('Yes')