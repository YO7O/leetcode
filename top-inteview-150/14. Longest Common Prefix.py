class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(ans) and i < len(s) and s[i] == ans[i]:
                i += 1
            ans = ans[:i]
        return ans
        # can sort strs in lexicographically then only compare first and last