class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        end = 0
        for i in range(len(nums)-k+1):
            end = max(end, i)
            while end+1 < len(nums) and nums[end]+1 == nums[end+1]:
                end += 1
            power = nums[i+k-1] if end >= i+k-1 else -1
            ans.append(power)
        return ans