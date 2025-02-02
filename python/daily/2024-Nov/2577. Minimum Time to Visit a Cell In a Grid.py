class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        prioQ = [(0, 0, 0)]
        while prioQ:
            time, i, j = heappop(prioQ)
            time += 1
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    visited[r][c] = True
                    gridrc = grid[r][c] if (grid[r][c] - time) % 2 == 0 else grid[r][c] + 1
                    newTime = max(time, gridrc)
                    if r == m-1 and c == n-1:
                        return newTime
                    heappush(prioQ, (newTime, r, c))

        return 0