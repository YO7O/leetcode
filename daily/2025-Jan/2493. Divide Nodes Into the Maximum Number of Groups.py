class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node: int, color: int) -> bool:
            if color == 0:
                color = 1
            elif colors[node] != 0:
                if colors[node] == color:
                    return True
                return False
            
            bipartite = True
            colors[node] = color
            for nextt in graph[node]:
                bipartite = bipartite and dfs(nextt, -color)
            return bipartite

        def bfs(src: int, group: int) -> List[int]:
            if groups[src]:
                group = groups[src]

            visited = [False] * (n + 1)
            queue = deque([src])
            visited[src] = True
            distance = 0

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    groups[node] = group
                    for nextt in graph[node]:
                        if not visited[nextt]:
                            visited[nextt] = True
                            queue.append(nextt)
                distance += 1

            return (distance, group)

        colors = [0] * (n + 1)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        graph = [[] for _ in range(n + 1)]
        groups = [0] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(1, n + 1):
            if colors[node] == 0 and not dfs(node, 0):
                return -1

        nextGroup = 1
        groupMax = [0]
        for node in range(1, n + 1):
            length, group = bfs(node, nextGroup)
            if nextGroup == group:
                groupMax.append(0)
                nextGroup += 1
            groupMax[group] = max(groupMax[group], length)

        return sum(groupMax)
