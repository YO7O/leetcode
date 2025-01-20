class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[-1] * m for _ in range(n)]
        queue = [deque([(0, 0)]), deque([])]
        
        curcost = 0
        while queue[0]:
            while queue[0]:
                i, j = queue[0].popleft()
                if dp[i][j] != -1:
                    continue
                dp[i][j] = curcost
                for d in range(4):
                    r, c = i + directions[d][0], j + directions[d][1]
                    if 0 <= r < n and 0 <= c < m and dp[r][c] == -1:
                        if d + 1 == grid[i][j]:
                            queue[0].append((r, c))
                        else:
                            queue[1].append((r, c))
            queue.reverse()
            curcost += 1
        
        return dp[-1][-1]