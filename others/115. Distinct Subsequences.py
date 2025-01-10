class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0
        dp = [[0] * n for _ in range(2)]

        for j in range(n):
            dp[1][j] = dp[1][j-1]
            if s[j] == t[0]:
                dp[1][j] += 1

        for i in range(1, m):
            dp.reverse()
            dp[1][i] = dp[0][i-1] if s[i] == t[i] else 0
            for j in range(i+1, n):
                dp[1][j] = dp[1][j-1]
                if s[j] == t[i]:
                    dp[1][j] += dp[0][j-1]

        return dp[1][-1]