class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        dp = [-1] * n # -1: not visited, 0: visiting, 1: safe, 2: not safe

        def dfs(node: int) -> bool:
            if dp[node] != -1:
                return dp[node] == 1
            
            dp[node] = 0
            safe = True
            for nextt in graph[node]:
                safe = safe and dfs(nextt)
            dp[node] = 1 if safe else 2
            return safe
        
        for node in range(n):
            dfs(node)
        
        return [node for node in range(n) if dp[node] == 1]