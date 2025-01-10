class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def pathExistHelper(i: int, j: int) -> bool:
            """
            prerequesite: board[i][j] == 0
            """
            path = False
            if i == 0:
                path = True
            else:
                for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                    r, c = i + x, j + y
                    if 0 <= r < row and 0 <= c < col:
                        path = path or pathExist[r][c]
            
            if not path:
                return False

            return pathUpdate(i, j)

            
        def pathUpdate(i: int, j: int) -> bool:
            """
            prerequesite:   board[i][j] == 0
                            pathExist[i][j] == True
            return: True if path reaches bottom
                    False otherwise
            """
            if i == row - 1:
                return True
            if pathExist[i][j]:
                return False
            pathExist[i][j] = True
            bottom = False

            for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                r, c = i + x, j + y
                if 0 <= r < row and 0 <= c < col and board[r][c] == 0:
                    bottom = bottom or pathUpdate(r, c)
            return bottom


        pathExist = [[False] * col for _ in range(row)]
        board = [[1] * col for _ in range(row)]
        for pos in range(row * col - 1, -1, -1):
            i, j = cells[pos]
            i, j = i - 1, j - 1
            board[i][j] = 0 
            if pathExistHelper(i, j):
                return pos

        return 0
