class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 1
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff > 0:
                inc += 1
                dec = 1
            elif diff < 0:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, dec, inc)
        
        return ans