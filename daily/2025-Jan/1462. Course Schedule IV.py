class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(course: int) -> None:
            if visited[course]:
                return

            for p in pre[course]:
                dfs(p)
                pre[course] = pre[course].union(pre[p])
            visited[course] = True
            return


        pre = [set() for _ in range(numCourses)]
        degree = [[0, i] for i in range(numCourses)]
        visited = [False] * numCourses

        for u, v in prerequisites:
            pre[v].add(u)

        for i in range(numCourses):
            dfs(i)

        ans = []
        for u, v in queries:
            ans.append(u in pre[v])

        return ans