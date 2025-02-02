class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        lst = []
        ans = maxx = 0
        for start, end, val in events:
            lst.append((start, True, val)) # time, isStart, val
            lst.append((end + 1, False, val)) # end + 1 for incluesive
        lst.sort()

        for time, isStart, val in lst:
            if isStart:
                ans = max(ans, maxx + val)
            else:
                maxx = max(maxx, val)

        return ans