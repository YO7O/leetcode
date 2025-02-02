class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = len(nums)+1
        cur = 0
        queue = deque([(0, 0)])
        for i in range(len(nums)):
            cur += nums[i]
            while queue and cur - queue[0][1] >= k:
                ans = min(ans, i-queue.popleft()[0]+1)
            while queue and cur <= queue[-1][1]:
                queue.pop()
            queue.append((i+1, cur))

        return ans if ans != len(nums)+1 else -1