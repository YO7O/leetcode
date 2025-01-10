class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        leftmost = [n] * 26
        rightmost = [-1] * 26

        for i, c in enumerate(s):
            pos = ord(c) - ord('a')
            leftmost[pos] = min(leftmost[pos], i)
            rightmost[pos] = max(rightmost[pos], i)
        
        ans = 0

        for i in range(26):
            if leftmost[i] == n:
                continue
            
            table = set()
            for j in range(leftmost[i] + 1, rightmost[i]):
                table.add(s[j])
            
            ans += len(table)

        return ans