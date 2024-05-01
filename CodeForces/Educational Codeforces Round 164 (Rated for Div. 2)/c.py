t = int(input())
mod = 1e9 + 7
for i in range(t):
    n, k = map(int, input().split())
    dp = [0 for i in range(n + 1)]
    dp[0] = dp[1] = 1
    pre = 0
    for j in range(k):
        r, c = map(int, input().split())
        if r == c:
            pre += 1
        else:
            pre += 2
    left = n - pre
    for j in range(2, left + 1):
        dp[j] = (dp[j - 1] + 2 * (j - 1) * dp[j - 2] % mod) % mod
    print(int(dp[left]))
