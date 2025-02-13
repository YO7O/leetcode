class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = cur = ans = 0
        for num in nums:
            if num > last:
                cur += num
                ans = max(ans, cur)
            else:
                cur = num
            last = num
        return ans