n, piplen = map(int, input().split())
gatelist = []
for i in range(n):
    gatelist.append(list(map(int, input().split())))


def ans_check(ans: int):
    flowlist = []
    for i in range(n):
        if gatelist[i][1] > ans:
            continue
        l = max(1, gatelist[i][0] - (-gatelist[i][1] + ans))
        r = min(piplen, gatelist[i][0] + (-gatelist[i][1] + ans))
        flowlist.append([l, r])
    flowlist.sort()
    if flowlist[0][0] > 1:
        return False
    lr = flowlist[0][1]
    for i in range(1, len(flowlist)):
        if flowlist[i][0] > lr and lr + 1 != flowlist[i][0]:
            return False
        else:
            lr = max(flowlist[i][1], lr)
    if lr < piplen:
        return False
    return True


gl = 1
gr = 2 * 10**9+1
while gl + 1 != gr:
    mid = (gl + gr) // 2
    if ans_check(mid):
        gr = mid
    else:
        gl = mid

print(gr)
