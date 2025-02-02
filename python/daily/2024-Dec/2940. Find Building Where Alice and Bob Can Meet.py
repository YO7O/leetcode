class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        h, q = len(heights), len(queries)
        ans = [-1] * q
        stack = []
        newQueries = []

        for i in range(q):
            a, b = queries[i] if queries[i][0] <= queries[i][1] else reversed(queries[i])
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                newQueries.append([b, heights[a], i])

        if not newQueries:
            return ans

        newQueries.sort()
        nqpos = len(newQueries) - 1

        for j in range(h-1, -1, -1):
            while stack and stack[-1][0] <= heights[j]:
                stack.pop()
            stack.append((heights[j], j))

            s = len(stack)
            left = 0
            while nqpos >= 0 and j == newQueries[nqpos][0]:
                p, height, i = newQueries[nqpos]
                if height >= stack[0][0]:
                    nqpos -= 1
                    continue

                right = s
                while left < right:
                    mid = (left + right) // 2
                    if stack[mid][0] > height:
                        left = mid + 1
                    else:
                        right = mid
                ans[i] = stack[left-1][1]
                nqpos -= 1

        return ans