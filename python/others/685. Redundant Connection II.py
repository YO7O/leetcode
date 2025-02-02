class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        root = child = 0
        for i in range(n + 1):
            if degree[i] == 0:
                root = i
            elif degree[i] == 2:
                child = i
        
        visited = [-1] * (n + 1)
        cycle = set()
        def dfs(cur: int) -> int:
            if visited[cur] == 0:
                visited[cur] = 1
                return cur
            if visited[cur] == 1:
                return -1

            visited[cur] = 0
            for nextt in graph[cur]:
                tmp = dfs(nextt)
                if tmp == -1:
                    continue
                if tmp == -2:
                    visited[cur] = 1
                    return -2
                
                if tmp == cur:
                    cycle.add((cur, nextt))
                    visited[cur] = 1
                    return -2
                cycle.add((cur, nextt))
                visited[cur] = 1
                return tmp

            visited[cur] = 1
            return -1

        if child != 0:
            dfs(child)
        else:
            for i in range(1, n + 1):
                if dfs(i) == -2:
                    break
        
        if cycle:
            if child == 0:
                for i in range(n - 1, -1, -1):
                    u, v = edges[i]
                    if (u, v) in cycle:
                        return [u, v]
            
            for i in range(n - 1, -1, -1):
                u, v = edges[i]
                if child == v and (u, v) in cycle:
                    return [u, v]
        
        for i in range(n - 1, -1, -1):
            u, v = edges[i]
            if v == child:
                return [u, v]
        
        return []