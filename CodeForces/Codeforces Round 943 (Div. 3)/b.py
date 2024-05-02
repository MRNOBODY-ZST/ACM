t = int(input())
for _ in range(t):
    len_a,len_b = map(int,input().split())
    a = input()
    b = input()
    a_pos = 0
    b_pos = 0
    exp = 0
    while a_pos < len_a and b_pos < len_b:
        if a[a_pos] == b[b_pos]:
            exp += 1
            a_pos += 1
            b_pos += 1
        else:
            b_pos += 1
    print(exp)
