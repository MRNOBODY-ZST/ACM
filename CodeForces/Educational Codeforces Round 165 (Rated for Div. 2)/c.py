for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(k + 1):
        dp[n - 1][i] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(k + 1):
            dp[i][j] = arr[i] + dp[i + 1][j]
            mn = arr[i]
            cnt = 0
            for l in range(i, i + j + 1):
                if l <= n - 1:
                    if arr[l] < mn:
                        mn = arr[l]
                        cnt = 1
                    elif arr[l] == mn:
                        cnt += 1
                    total = l - i + 1
                    if l + 1 <= n - 1:
                        dp[i][j] = min(
                            dp[i][j], mn * total + dp[l + 1][j - (total - cnt)]
                        )
                    else:
                        dp[i][j] = min(dp[i][j], mn * total)
    print(dp[0][k])
