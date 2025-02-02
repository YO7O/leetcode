class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def dfs(u: int, exclude: int) -> List[int]:
            summ = 0
            totalSplit = 0
            for v in graph[u]:
                if v == exclude:
                    continue
                psum, split = dfs(v, u)
                if psum % k == 0:
                    split += 1

                summ += psum
                totalSplit += split

            return [summ + values[u], totalSplit]


        graph = [[] for _ in range(n+1)]
        total = sum(values)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        

        return dfs(0, n)[1] + 1