class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        minStack, maxStack = deque([]),  deque([])
        start = 0
        for end in range(n):
            while minStack and nums[end] <= minStack[-1][1]:
                minStack.pop()
            minStack.append((end, nums[end]))
            while maxStack and nums[end] >= maxStack[-1][1]:
                maxStack.pop()
            maxStack.append((end, nums[end]))

            while maxStack and minStack and maxStack[0][1] - minStack[0][1] > 2:
                ans += end - start
                if maxStack[0][0] == start:
                    maxStack.popleft()
                if minStack[0][0] == start:
                    minStack.popleft()
                start += 1

        while start < n:
            ans += n - start
            start += 1

        return ans