from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    card_list = list(map(int,input().split()))
    card_set = list(set(card_list))
    tmp = Counter(card_list)
    point = 0
    for card in card_set:
        if tmp[card]>1:
            point+=1
    print(point)