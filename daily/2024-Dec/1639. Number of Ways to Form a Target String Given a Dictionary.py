class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        w = len(words[0])
        t = len(target)
        dp = [[0] * w for _ in range(t)]
        mod = 1000000007

        count = [[0] * 26 for _ in range(w)]
        for j in range(w):
            for word in words:
                count[j][ord(word[j]) - ord('a')] += 1

        # dp[0][0]
        dp[0][0] = count[0][ord(target[0]) - ord('a')]

        # dp[0][j]
        for j in range(1, w):
            dp[0][j] = dp[0][j-1] + count[j][ord(target[0]) - ord('a')]
                
        # dp[i][j], i >= 1, j >= 1
        for i in range(1, t):
            for j in range(i, w):
                dp[i][j] = (count[j][ord(target[i]) - ord('a')] * dp[i-1][j-1] + dp[i][j-1]) % mod
            
        return dp[-1][-1]