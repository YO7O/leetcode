class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums)
        for i in range(n-k):
            heappop(nums)
        return nums[0]