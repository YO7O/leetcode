class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # idea: https://leetcode.com/problems/trapping-rain-water-ii/solutions/1138028/python3-visualization-bfs-solution-with-explanation
        
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        heap = []

        for j in range(m):
            heap.append([heightMap[0][j], 0, j])
            heap.append([heightMap[-1][j], n-1, j])
            visited[0][j] = visited[-1][j] = True
        
        for i in range(1, n-1):
            heap.append([heightMap[i][0], i, 0])
            heap.append([heightMap[i][-1], i, m-1])
            visited[i][0] = visited[i][-1] = True
        
        ans = 0
        heapify(heap)

        while heap:
            h, x, y = heappop(heap)
            for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
                r, c = x + i, y + j
                if r < 0 or r >= n or c < 0 or c >= m or visited[r][c]:
                    continue
                visited[r][c] = True
                if h - heightMap[r][c] > 0:
                    ans += h - heightMap[r][c]
                    heappush(heap, [h, r, c])
                else:
                    heappush(heap, [heightMap[r][c], r, c])
        
        return ans