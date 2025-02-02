class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        ans = sys.maxsize
        botLeft, topRight = 0, sum(grid[0])
        for i in range(n):
            topRight -= grid[0][i]
            ans = min(ans, max(botLeft, topRight))
            botLeft += grid[1][i]

        return ans