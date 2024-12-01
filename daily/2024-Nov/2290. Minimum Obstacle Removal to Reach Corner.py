class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        checked = [[False] * n for _ in range(m)]
        queue = [deque([(0, 0)]), deque([])]
        step = 0

        while queue[0]:
            while queue[0]:
                i, j = queue[0].popleft()

                for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= r < m and 0 <= c < n and not checked[r][c]:
                        wall = grid[r][c]
                        checked[r][c] = True

                        if r == m-1 and c == n-1:
                            return step + wall
                        queue[wall].append((r, c))

            queue.reverse()
            step += 1

        return 0