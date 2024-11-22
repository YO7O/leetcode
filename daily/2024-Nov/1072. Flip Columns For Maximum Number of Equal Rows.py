class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Longer version
        
        # m = len(matrix)
        # n = len(matrix[0])
        # table = Counter()
        # for i in range(m):
        #     flip = matrix[i][0]
        #     for j in range(n):
        #         matrix[i][j] = matrix[i][j] ^ flip
        #     s = tuple(matrix[i])
        #     table[s] += 1
        
        # ans = max(table.values())

        return max(Counter(tuple(cell ^ row[0] for cell in row) for row in matrix).values())

        # faster(?) but less readable
        # most common gives a list of largest number, so get the first items value: [0][1]
        # return Counter(tuple(cell ^ row[0] for cell in row) for row in matrix).most_common(1)[0][1]