class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if dp[i][j] != -1:
                return dp[i][j]

            maxx = 0
            for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                r, c = i + x, j + y
                if 0 <= r < n and 0 <= c < m and matrix[r][c] < matrix[i][j]:
                    maxx = max(maxx, dfs(r, c))
            dp[i][j] = maxx + 1
            return maxx + 1
                

        n, m = len(matrix), len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        
        return ans