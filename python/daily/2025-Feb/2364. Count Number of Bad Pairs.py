class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        table = {}
        for i in range(n):
            diff = nums[i] - i
            if diff in table:
                table[diff] += 1
            else:
                table[diff] = 1
        
        ans = (n * (n - 1)) // 2
        for dup in table.values():
            ans -= (dup * (dup - 1)) // 2
        
        return ans