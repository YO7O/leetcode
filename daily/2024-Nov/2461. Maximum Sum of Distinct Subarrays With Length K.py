class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = 0
        end = 0
        table = {}
        cur = 0
        ans = 0

        while start <= n-k:
            while end < start+k:
                if nums[end] in table:
                    break
                table[nums[end]] = True
                cur += nums[end]
                end += 1
                
            
            if end-start == k:
                ans = max(ans, cur)
            cur -= nums[start]
            table.pop(nums[start])
            start += 1

        return ans
