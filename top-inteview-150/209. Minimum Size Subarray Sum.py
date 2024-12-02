class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, summ = 0, 0
        n = len(nums)
        ans = n + 1
        for end in range(n):
            summ += nums[end]
            while summ >= target:
                ans = min(ans, end-start+1)
                summ -= nums[start]
                start += 1
        return ans if ans != n + 1 else 0
