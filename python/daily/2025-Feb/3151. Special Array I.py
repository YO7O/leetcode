class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all([nums[i] & 1 != nums[i - 1] & 1 for i in range(1, len(nums))])