class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + max(zero, one) + 1)
        dp[-1] = 1

        for i in range(high + 1):
            dp[i] = (dp[i-zero] + dp[i-one]) % 1000000007
        return sum(dp[low-1:high]) % 1000000007
        