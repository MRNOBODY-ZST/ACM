from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    a_dict = Counter(a)
    for j in a_dict.keys():
        if a_dict[j] > 2:
            cnt += a_dict[j]//3
    print(cnt)