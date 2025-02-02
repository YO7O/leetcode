class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > k * 2:
                left += 1
            ans = max(ans, right - left + 1)

        return ans