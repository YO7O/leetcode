class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minn = 100000
        summ = 0
        negativeCount = 0
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negativeCount += 1
                summ += abs(matrix[i][j])
                minn = min(minn, abs(matrix[i][j]))
        
        if negativeCount % 2 == 0:
            return summ
        return summ - 2 * minn