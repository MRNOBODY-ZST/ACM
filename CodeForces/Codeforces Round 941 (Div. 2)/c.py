t = int(input())

for _ in range(t):
    n = input()
    a = list(map(int, input().split()))
    a.sort()
    mexsize = 1
    maxsize = max(a)
    for i in range(len(a)):
        if a[i] == i:
            mexsize += 1
    if mexsize > maxsize:
        if maxsize % 2 == 1:
            print("Alice")
        else:
            print("Bob")
    else:
        if mexsize % 2 == 1:
            print("Alice")
        else:
            print("Bob")
