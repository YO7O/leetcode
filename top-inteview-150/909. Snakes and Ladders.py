class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        step = [-1] * (n * n + 1)
        step[1] = 0
        bfs = [1]
        for curr in bfs:
            for i in range(curr + 1, curr + 7):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0:
                    i = nxt
                if i == n*n:
                    return step[curr] + 1
                if step[i] == -1:
                    step[i] = step[curr] + 1
                    bfs.append(i)
        return -1
