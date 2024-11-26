class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(d) for row in board for d in row)
        queue = deque([s])
        table = {s: True}
        step = 0
        height, width = 2, 3
        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                if state == '123450':
                    return step
                i = state.index('0')
                y = i // width
                x = i % width
                for r, c in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                    if 0 <= r < width and 0 <= c < height:
                        ch = [d for d in state]
                        ch[i], ch[r+c*width] = ch[r+c*width], ch[i]
                        s = ''.join(ch)
                        if s not in table:
                            queue.append(s)
                            table[s] = True
            step += 1
        return -1