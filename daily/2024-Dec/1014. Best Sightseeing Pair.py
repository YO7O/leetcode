class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max1 = 0
        max2 = 0
        for value in values:
            max2 = max(max2, max1 + value)
            max1 = max(max1, value) - 1
        return max2