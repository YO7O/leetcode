class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax = 0
        curMax = nums[0]
        curBit = nums[0].bit_count()
        for i in range(1, len(nums)):
            b = nums[i].bit_count()
            if curBit != b:
                prevMax = curMax
                curBit = b
                curMax = nums[i]
            else:
                curMax = max(nums[i], curMax)
            if nums[i] < prevMax:
                return False
        return True