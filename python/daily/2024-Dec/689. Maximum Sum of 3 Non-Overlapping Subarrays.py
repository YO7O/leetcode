class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [[-1, -1] for _ in range(n)] # sum, pos
        right = [[-1, n] for _ in range(n)]
        ans = [-1, -1, -1]

        cur = sum(nums[:k])
        maxx = cur
        maxpos = 0
        for i in range(k, n):
            if maxx < cur:
                maxx = cur
                maxpos = i-k
            left[i][0] = maxx
            left[i][1] = maxpos
            cur += nums[i] - nums[i-k]
        
        cur = sum(nums[n-k:])
        maxx = cur
        maxpos = n-k
        for i in range(n-k, k-1, -1):
            if maxx <= cur:
                maxx = cur
                maxpos = i
            right[i-k][0] = maxx
            right[i-k][1] = maxpos
            cur += nums[i-1] - nums[i+k-1]

        cur = sum(nums[k:k*2])
        maxx = 0
        for i in range(k, n-k):
            cur += nums[i+k-1] - nums[i-1]
            cursum = left[i][0] + cur + right[i][0]
            if maxx < cursum:
                maxx = cursum
                ans = [left[i][1], i, right[i][1]]
        

        
        return ans