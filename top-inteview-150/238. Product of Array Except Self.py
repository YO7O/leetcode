class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        cur = 1
        for i in range(len(nums)):
            ans[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= cur
            cur *= nums[i]
        return ans