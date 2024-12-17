class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        lst = sorted(enumerate(nums), key = itemgetter(1))
        marked = [False] * n
        ans = 0

        for pos, num in lst:
            if marked[pos]:
                continue
            for i in range(-1,2):
                npos = pos + i
                if 0 <= npos < n:
                    marked[npos] = True
            ans += num

        return ans