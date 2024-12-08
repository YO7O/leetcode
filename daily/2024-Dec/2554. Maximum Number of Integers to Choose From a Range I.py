class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        table = [-1] * (n + 1)
        ans = 0
        summ = 0

        for num in banned:
            if num > n or table[num] != -1:
                continue
            
            table[num] = 1

        
        for num in range(1, n+1):
            if table[num] != -1:
                table[num] = 1
                continue

            summ += num
            if summ > maxSum:
                return ans
            ans += 1
                
        return ans