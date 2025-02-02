class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)
        while left < right:
            x = (left + right) // 2
            if sum(ceil(q/x) for q in quantities) > n:
                left = x + 1
            else:
                right = x
        return left