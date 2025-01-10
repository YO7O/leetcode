class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 1000000007
        dp = [0] * 26
        a = ord('a')
        total = 0

        for c in s:
            pos = ord(c) - a
            temp = total - dp[pos]
            dp[pos] = (total + 1) % mod
            total = (temp + dp[pos]) % mod

        return total