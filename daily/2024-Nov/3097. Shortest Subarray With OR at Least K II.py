class Solution:
    def __init__(self) -> None:
        self.bits = [0] * 30

    def increase(self, num: int) -> None:
        pos = 0
        while num != 0:
            if num & 1:
                self.bits[pos] += 1
            num >>= 1
            pos += 1

    def decrease(self, num: int) -> int:
        pos = 0
        removed = 0
        bit = 1
        while num != 0:
            if num & 1:
                self.bits[pos] -= 1
                if not self.bits[pos]:
                    removed += bit
            pos += 1
            num >>= 1
            bit <<= 1
        return removed

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
            
        start = 0
        ans = len(nums)+1
        curOr = 0

        for end in range(len(nums)):
            curOr |= nums[end]
            self.increase(nums[end])
            while curOr >= k:
                curOr -= self.decrease(nums[start])
                start += 1
            if start > 0 and curOr | nums[start-1] >= k:
                ans = min(ans, end-start+2)

        return ans if ans != len(nums)+1 else -1
