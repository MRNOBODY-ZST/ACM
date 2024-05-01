cnt = 0
for i in range(1,100000000):
    str_i = str(i)
    sum_h = 0
    sum_l = 0
    if len(str_i)%2 != 0:
        continue
    else:
        for j in range(len(str_i)):
            if j< len(str_i)/2:
                sum_h += int(str_i[j])
            else:
                sum_l += int(str_i[j])
        if sum_h == sum_l:
            cnt+=1
print(cnt)