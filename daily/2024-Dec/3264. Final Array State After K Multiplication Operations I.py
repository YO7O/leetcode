class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        while k > 0:
            num, i = heap[0]
            nums[i] = num * multiplier
            heapreplace(heap, (num * multiplier, i))
            k -= 1

        return nums