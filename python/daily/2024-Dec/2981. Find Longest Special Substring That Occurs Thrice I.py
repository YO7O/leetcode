class Solution:
    def maximumLength(self, s: str) -> int:
        table = Counter()
        left = 0
        n = len(s)
        for i in range(1, n):
            if s[i] != s[i-1]:
                m = i - left
                temp = s[i-1]
                for j in range(m):
                    table[temp] += m - j
                    temp += s[i-1]
                left = i
        
        m = n - left
        temp = s[i]
        for j in range(m):
            table[temp] += m - j
            temp += s[i]

        ans = 0
        for ss in table:
            if table[ss] >= 3:
                ans = max(ans, len(ss))

        return ans if ans != 0 else -1