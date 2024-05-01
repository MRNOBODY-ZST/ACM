t = int(input())
for i in range(t):
    bin_str = input()
    length = len(bin_str)
    zeros = 0
    cost = 0
    for i in range(length):
        if bin_str[i] != '0':
            break
        zeros += 1
    for i in range(zeros,length):
        if bin_str[i] == '0':
            cost += i - zeros + 1
            zeros += 1
    print(cost)