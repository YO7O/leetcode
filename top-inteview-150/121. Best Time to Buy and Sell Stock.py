class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for price in prices:
            if stack and stack[-1] > price:
                ans = max(ans, stack[-1] - stack[0])
                while stack and stack[-1] > price:
                    stack.pop()
            stack.append(price)
        ans = max(ans, stack[-1] - stack[0])
        return ans