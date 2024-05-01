cnt = 0
def num_find(num:int):
    pattern_list = ['2','0','2','3']
    tmp = str(num)
    num_index = 0
    for j in range(4):
        num_index = tmp.find(pattern_list[j],num_index)
        if num_index == -1:
            return False
    return True
for i in range(12345678,98765433):
    if num_find(i) == False:
        cnt+=1
print(cnt)