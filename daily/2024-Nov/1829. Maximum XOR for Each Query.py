class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = (1 << maximumBit) - 1
        q = 0
        ans = []
        for i in range(len(nums)):
            q = q ^ nums[i]
            ans.append(m^q)
        ans.reverse()
        return ans