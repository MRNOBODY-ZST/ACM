n = int(input())
matrix = {}
for i in range(n):
    tmp1 = list(map(int, input().split()))
    tmp2 = list(map(int, input().split()))
    matrix_sum = sum(tmp2)
    if matrix_sum % (tmp1[0]**2) == 0:
        print('YES')
    else:
        print('NO')