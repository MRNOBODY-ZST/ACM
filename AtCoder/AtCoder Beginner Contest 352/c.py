n = int(input())
a_list = [0 for _ in range(n)]
b_list = [0 for _ in range(n)]
min_pos = 0
tmp = 0
for i in range(n):
    a, b = map(int, input().split())
    a_list[i] = a
    b_list[i] = b
    minus = b - a
    if tmp < minus:
        tmp = minus
        min_pos = i
print(str(sum(a_list) - a_list[min_pos] + b_list[min_pos]))
