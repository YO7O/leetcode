class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        nodes = [-1] * n
        for u, v in edges:
            if nodes[u] == -1:
                nodes[u] = 1

            if nodes[v] == -1:
                nodes[v] = 0
            else:
                nodes[v] = 0
        
        champion = -1
        for i in range(n):
            if nodes[i] == -1:
                return -1
            elif nodes[i] == 1:
                if champion != -1:
                    return -1
                champion = i
        
        return champion