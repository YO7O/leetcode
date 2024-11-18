class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = [-1] * len(nums)
        step[0] = 0
        end = 0
        for i in range(len(nums)):
            if i+nums[i] >= len(nums)-1:
                return step[i]+1
            while end < i+nums[i]:
                end += 1
                step[end] = step[i]+1

        return -1