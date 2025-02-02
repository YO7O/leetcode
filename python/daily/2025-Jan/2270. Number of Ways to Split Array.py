class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = (total + 1) // 2
        cur, ans = 0, 0
        
        for i in range(len(nums) - 1):
            cur += nums[i]
            if cur >= target:
                ans += 1

        return ans