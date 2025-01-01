class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def ftf(graph: List[List[int]]) -> int:
            level = deque([0])
            node = -1
            visited = [False] * len(graph)

            while level:
                nextLevel = deque([])
                while level:
                    node = level.popleft()
                    visited[node] = True
                    for n in graph[node]:
                        if not visited[n]:
                            nextLevel.append(n)
                level = nextLevel

                
            level = deque([node])
            visited = [False] * len(graph)
            length = 0

            while level:
                nextLevel = deque([])
                while level:
                    node = level.popleft()
                    visited[node] = True
                    for n in graph[node]:
                        if not visited[n]:
                            nextLevel.append(n)
                level = nextLevel
                length += 1


            return length - 1


        graph1 = [[] for _ in range(len(edges1) + 1)]
        graph2 = [[] for _ in range(len(edges2) + 1)]
        
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        d1 = ftf(graph1)
        d2 = ftf(graph2)
            
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)