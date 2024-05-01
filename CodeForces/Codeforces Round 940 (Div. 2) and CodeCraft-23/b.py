t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    a = []
    cnt = 0
    num_cnt = 0
    tmp = ''
    if n == 1:
        print(k)
    else:
        for j in range(0,k+1):
            cnt = 2**j
            if cnt > k:
                a.append((str(2**(j-1)-1)+' '))
                num_cnt += 1
                break
        a.append(str(k-(2**(j-1)-1))+' ')
        num_cnt += 1
        if num_cnt < n:
            for j in range(num_cnt,n):
                a.append('0 ')
        print(tmp.join(a))