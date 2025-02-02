class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        jstart = len(nums) - 1
        jend = jstart
        ans = 0
        for i in range(len(nums)):
            while jend > i and nums[i] + nums[jend] > upper:
                jend -= 1
            if jend <= i:
                break
            if jstart > jend:
                jstart = jend

            while jstart > i and nums[i] + nums[jstart] >= lower:
                jstart -= 1
            if jstart <= i:
                jstart = i

            ans += jend - jstart
        return ans