class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
            
        i = 0
        n = len(s)
        for c in t:
            if c == s[i]:
                i += 1
                if i >= n:
                    return True
        return False