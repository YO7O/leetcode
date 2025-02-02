class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx = -1
        ans = 0
        for i in range(len(arr)):
            maxx = max(maxx, arr[i])
            if maxx == i:
                ans += 1
        return ans
