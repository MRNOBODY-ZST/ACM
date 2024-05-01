money = [i for i in range(2024)]+[0 for i in range(2024,4047)]
for i in range(1,2024):
    for j in range(i,2024):
        if i==j:
            money[j+i]+=i//2
        else:
            money[j+i]+=i
print(max(money))