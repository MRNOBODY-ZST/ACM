s = [0] + list(input())
for i in range(1, len(s)):
    s[i] = ord(s[i]) - 96
dp = [0] * (len(s) + 1)
dp[1] = s[1]
for i in range(2, len(s)):
    dp[i] = max(dp[i - 1], dp[i - 2] + s[i])
print(dp[len(s) - 1])
