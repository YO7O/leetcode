class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        nboard = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                neighbours = 0
                for x, y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    r, c = i + x, j + y
                    if 0 <= r < n and 0 <= c < m:
                        neighbours += board[r][c]
                if board[i][j] == 1 and (2 <= neighbours <= 3):
                    nboard[i][j] = 1
                elif board[i][j] == 0 and neighbours == 3:
                    nboard[i][j] = 1

        print(nboard)
        for i in range(n):
            for j in range(m):
                board[i][j] = nboard[i][j]
