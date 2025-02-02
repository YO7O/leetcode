class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(last: int, cur: int) -> int:
            if visited[cur]:
                return cur

            visited[cur] = True
            inCycle = -1
            for nextt in graph[cur]:
                if last == nextt:
                    continue
                tmp = dfs(cur, nextt)
                if tmp != -1:
                    cycle.add((cur, nextt))
                    if tmp != cur:
                        inCycle = tmp
                    break

            return inCycle
        
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        cycle = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dfs(0, 1)
        
        for i in range(n - 1, -1, -1):
            u, v = edges[i]
            if (u, v) in cycle or (v, u) in cycle:
                return (u, v)