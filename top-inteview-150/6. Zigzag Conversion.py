class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        array = [""] * numRows
        row = 0
        x = -1
        for c in s:
            array[row] += c
            if row == 0 or row == numRows-1:
                x = -x
            row += x
        return ''.join(array)