class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                count[nums[i] * nums[j]] += 1
        
        ans = 0
        for freq in count.values():
            ans += ((freq - 1) * freq) // 2
        
        return ans * 8