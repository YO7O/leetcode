class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        dp = [[False] * n for _ in range(m)]
        for row in range(m):
            dp[row][0] = True
        for col in range(1, n):
            cont = False
            for row in range(m):
                if (row > 0 and dp[row-1][col-1] and grid[row-1][col-1] < grid[row][col]) or (dp[row][col-1] and grid[row][col-1] < grid[row][col]) or (row < m-1 and dp[row+1][col-1] and grid[row+1][col-1] < grid[row][col]):
                    dp[row][col] = True
                    cont = True
            if not cont:
                return col-1
        return n-1