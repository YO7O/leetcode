class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:            
        # 0: not guarded, 1: guarded, 2: guard, 3: wall
        horizontal = [[0] * n for _ in range(m)]
        vertical = [[0] * n for _ in range(m)]
        ans = m * n
        for i, j in walls:
            horizontal[i][j] = 3
            vertical[i][j] = 3

        for i, j in guards:
            horizontal[i][j] = 2
            vertical[i][j] = 2

            # horizontal
            col = j - 1
            while col >= 0 and horizontal[i][col] == 0:
                horizontal[i][col] = 1
                col -= 1
            col = j + 1
            while col < n and horizontal[i][col] == 0:
                horizontal[i][col] = 1
                col += 1
            
            # vertical
            row = i - 1
            while row >= 0 and vertical[row][j] == 0:
                vertical[row][j] = 1
                row -= 1
            row = i + 1
            while row < m and vertical[row][j] == 0:
                vertical[row][j] = 1
                row += 1
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += 1 if horizontal[i][j] == 0 and vertical[i][j] == 0 else 0
        return ans    