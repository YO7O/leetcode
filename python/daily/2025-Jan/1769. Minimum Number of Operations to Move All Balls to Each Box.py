class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * (n + 1)

        ones = 0
        for i in range(n):
            ans[i] = ans[i-1] + ones
            if boxes[i] == '1':
                ones += 1
        
        last, ones = 0, 0
        for i in range(n-1, -1, -1):
            last = last + ones
            ans[i] += last
            if boxes[i] == '1':
                ones += 1

        return ans[:-1]