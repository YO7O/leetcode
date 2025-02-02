class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ngifts = list(map(neg, gifts))
        heapify(ngifts)
        for i in range(k):
            heappushpop(ngifts, -isqrt(-ngifts[0]))

        return -sum(ngifts)