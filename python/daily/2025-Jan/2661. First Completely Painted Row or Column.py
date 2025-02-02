class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [True] * m, [True] * n
        rowcount, colcount = m, n
        pos = [(-1, -1) for _ in range(m * n + 1)]

        # Mapping positions
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)


        for i in range(m * n - 1, -1, -1):
            x, y = pos[arr[i]]
            # if rows is still connected, reduce connected row count
            if rows[x]:
                rowcount -= 1
            rows[x] = False
            # same for col
            if cols[y]:
                colcount -= 1
            cols[y] = False
            # there's neither connected row nor col
            if rowcount == 0 and colcount == 0:
                return i
        return 0