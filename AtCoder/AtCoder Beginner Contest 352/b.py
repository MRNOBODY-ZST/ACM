s = input()
t = input()
s_len = len(s)
t_len = len(t)
out_list = []
s_pos = 0
for i in range(t_len):
    if t[i] == s[s_pos]:
        s_pos += 1
        out_list.append(i + 1)

print(' '.join(map(str, out_list)))