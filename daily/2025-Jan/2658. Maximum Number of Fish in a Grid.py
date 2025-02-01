class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            fish = grid[i][j]
            grid[i][j] = 0
            for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                r, c = i + x, j + y
                if 0 <= r < m and 0 <= c < n:
                    fish += dfs(r, c)
            
            return fish
        
        m, n = len(grid), len(grid[0])
        
        ans = 0
        for i in range(m):
            for j in range(n):
               ans = max(ans, dfs(i, j))

        return ans 