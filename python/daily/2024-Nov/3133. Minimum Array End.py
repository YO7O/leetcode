class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        bit = 1
        while n > 0:
            if not bit & x:
                x |= (n & 1) * bit
                n >>= 1
            bit <<= 1
        return x