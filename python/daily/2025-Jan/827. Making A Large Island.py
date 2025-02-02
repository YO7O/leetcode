class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def area(i: int, j: int) -> None:
            if grid[i][j] == 0 or visited[i][j]:
                return


            island = len(islandArea)
            queue = deque([(i, j)])
            visited[i][j] = island
            area = 0
            while queue:
                i, j = queue.popleft()
                for x, y in directions:
                    r, c = i + x, j + y
                    if 0 <= r < n and 0 <= c < n and grid[r][c] and not visited[r][c]:
                        visited[r][c] = island
                        queue.append((r, c))
                area += 1
            
            islandArea.append(area)
            return

        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        islandArea = [0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(n):
                area(i, j)
        
        ans = max(islandArea)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                neighbors = []
                for x, y in directions:
                    r, c = i + x, j + y
                    if 0 <= r < n and 0 <= c < n and visited[r][c] not in neighbors:
                        neighbors.append(visited[r][c])
                ans = max(ans, sum([islandArea[neighbor] for neighbor in neighbors]) + 1)

        return ans