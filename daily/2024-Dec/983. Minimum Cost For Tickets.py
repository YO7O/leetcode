class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [[0] * 32 for _ in range(2)] # 0: last, 1: current
        dp[0][-1] = 2000000
        dp[1][-1] = 2000000

        for j in range(30, -1, -1):
            cost = 2000000
            if j == 30:
                cost = costs[2]
            elif j == 7:
                cost = costs[1]
            elif j == 1:
                cost = costs[0]
            dp[0][j] = min(cost, dp[0][j+1])

        for i in range(1, n):
            for j in range(30, -1, -1):
                cost = 2000000
                if j == 30:
                    cost = costs[2]
                if j == 7:
                    cost = costs[1]
                elif j == 1:
                    cost = costs[0]
                value1 = dp[0][j+days[i]-days[i-1]]if j+days[i]-days[i-1] <= 30 else 2000000
                value2 = dp[0][1] + cost
                dp[1][j] = min(value1, value2, dp[1][j+1])
            dp.reverse()
        
        return dp[0][1]