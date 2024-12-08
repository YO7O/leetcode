class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        start = 1
        end = max(nums)
        while start < end:
            mid = (start + end) // 2
            operations = 0
            for num in nums:
                operations += (num - 1) // mid

            if operations > maxOperations:
                start = mid + 1
            else:
                end = mid
        
        return start