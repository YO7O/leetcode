class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        m = len(pref)
        ans = 0
        for word in words:
            if len(word) >= m and word[:m] == pref:
                ans += 1
        
        return ans