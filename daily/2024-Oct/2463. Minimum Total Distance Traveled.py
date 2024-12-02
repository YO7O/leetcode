class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # TODO: understand O(mn) time complexity solution
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)
        dp = [inf] * (n + 1)
        dp[n] = 0

        # for each loop of j, dp[i] represents the minimum cost of fixing robot[i:] with factory[j:]
        for j in range(m-1, -1, -1):
            for i in range(n):
                cur = 0
                # fixing k robot in factory[j]
                for k in range(1, min(factory[j][1], n - i) + 1):
                    cur += abs(robot[i+k-1] - factory[j][0])
                    # cur: fixing robot[i:i+k] in factory[j] 
                    # dp[i+k]: fixing robot[i+k:] in factory[j+1:], NOTE: dp[i+k] has not updated
                    dp[i] = min(dp[i], dp[i+k] + cur)
        return dp[0]
        


#         # https://leetcode.com/problems/minimum-total-distance-traveled/solutions/2783305/python-dp-solution

#         # dp(i, j, k) means the cost that to fix
#         # robot[i:] with factory[j] that already fix k robot
#         # def dp(i: int, j: int, k: int) -> int:
#         #     if i == len(robot):
#         #         return 0
#         #     if j == len(factory):
#         #         return inf
            
#         #     # Don't fix robot[i] in factory[j]
#         #     res1 = dp(i, j + 1, 0)
#         #     # Fix robot[i] at factroy[j]
#         #     res2 = dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else inf
#         #     return min(res1, res2)
        
#         # return dp(0, 0, 0)