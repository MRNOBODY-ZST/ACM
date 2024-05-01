t = int(input())
tc = []
for _ in range(t):
    k,q = map(int,input().split())
    a = list(map(int,input().split()))
    n = list(map(int,input().split()))
    out = ''
    for num in n:
        while True:
            for index in a:
                if index<=num:
                    num-=1
            if a[0]>num:
                break
        out += str(num)+' '
    print(out)