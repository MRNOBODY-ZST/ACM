t = int(input())
for i in range(t):
    tmp = list(map(int, input().split()))
    if tmp[0] - (tmp[0] // tmp[1] + int(tmp[0] % tmp[1] != 0)) > tmp[2]:
        print("Yes")
    else:
        print("No")
