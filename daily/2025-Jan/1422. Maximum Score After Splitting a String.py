class Solution:
    def maxScore(self, s: str) -> int:
        c = Counter([c for c in s[1:]])
        cur = c['1'] if s[0] == '1' else c['1'] + 1
        ans = cur
        for i in range(1, len(s)-1):
            if s[i] == '0':
                cur += 1
            else:
                cur -= 1
            ans = max(ans, cur)
        return ans