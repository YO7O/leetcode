class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = deque([])
        height = [[-1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for x, y in (1, 0), (-1, 0), (0, 1), (0, -1):
                r, c = i + x, j + y
                if 0 <= r < m and 0 <= c < n and height[r][c] == -1:
                    height[r][c] = height[i][j] + 1
                    queue.append((r, c))

        return height