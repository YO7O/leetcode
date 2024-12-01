class Solution:
    def updateDistances(self, graph: List[List[int]], cur: int, dp: List[int]): 
        newDist = dp[cur] + 1

        for neighbor in graph[cur]:
            if dp[neighbor] <= newDist:
                continue

            dp[neighbor] = newDist
            self.updateDistances(graph, neighbor, dp)

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[i-1] for i in range(n)]
        graph[0].pop()
        dp = [i for i in range(n-1, -1, -1)]
        ans = []

        for u, v in queries:
            graph[v].append(u)
            newDist = dp[v] + 1

            if dp[u] > newDist:
                dp[u] = newDist
                self.updateDistances(graph, u, dp)
            
            ans.append(dp[0])

        return ans
