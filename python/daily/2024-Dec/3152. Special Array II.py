class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        subarray = [0] * n
        for i in range(1, n):
            subarray[i] = i if (nums[i] - nums[i-1]) % 2 == 0 else subarray[i-1]

        ans = []
        
        for start, end in queries:
            ans.append(start >= subarray[end])
        
        return ans