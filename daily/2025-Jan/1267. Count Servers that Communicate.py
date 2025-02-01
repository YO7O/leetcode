class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        commute = [[0] * n for _ in range(m)]
        ans = 0

        for row in range(m):
            server = [col for col in range(n) if grid[row][col]]
            if len(server) >= 2:
                for col in server:
                    commute[row][col] = 1
                    ans += 1

        for col in range(n):
            server = [row for row in range(m) if grid[row][col]]
            if len(server) >= 2:
                for row in server:
                    if commute[row][col] == 1:
                        continue
                    commute[row][col] = 1
                    ans += 1
            
        return ans