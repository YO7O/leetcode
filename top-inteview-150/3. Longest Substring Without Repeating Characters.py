class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        start, end, ans = 0, 0, 0
        for c in s:
            if c in table:
                while table[c]:
                    table[s[start]] = False
                    start += 1
            table[c] = True
            end += 1
            ans = max(ans, end-start)

        return ans