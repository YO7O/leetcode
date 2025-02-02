class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ans = 0
        if n % 2:
            for num in nums2:
                ans ^= num
        if m % 2:
            for num in nums1:
                ans ^= num
        
        return ans