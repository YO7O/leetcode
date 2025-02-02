class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        start = 0
        end = x // 2 + 1
        while start < end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid
            else:
                start = mid + 1
        return start - 1
