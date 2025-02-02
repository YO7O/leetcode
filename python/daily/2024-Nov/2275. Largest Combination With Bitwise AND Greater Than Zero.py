class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        bit = 1
        for i in range(26):
            count = sum(1 for candidate in candidates if candidate & bit)
            ans = max(ans, count)
            bit <<= 1
        return ans