class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = False
        for i in range(n):
            if nums[i] < nums[i - 1]:
                if rotated:
                    return False
                rotated = True
        
        return True