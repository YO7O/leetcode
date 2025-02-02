class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(target - num, -1, -1):
                if dp[i] == 0:
                    continue
                dp[i+num] += dp[i] 
        
        return dp[target]