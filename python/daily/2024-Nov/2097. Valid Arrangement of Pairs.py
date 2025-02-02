class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def dfs(node: int) -> None:
            while graph[node]:
                dfs(graph[node].pop())
            ans.append(node)


        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1
        
        for node in degree:
            if degree[node] == 1:
                u = node
                break
        
        
        ans = []
        dfs(u)
        ans.reverse()
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]