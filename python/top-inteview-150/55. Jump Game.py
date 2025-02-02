class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in range(len(nums)):
            if i > end:
                return False
            end = max(end, i+nums[i])
            if end >= len(nums):
                return True
        return True