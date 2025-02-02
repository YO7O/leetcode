class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = [0] * (len(words) + 1)
        cur = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                cur += 1
            dp[i] = cur
        
        ans = [0] * len(queries)

        for i, (start, end) in enumerate(queries):
            ans[i] = dp[end] - dp[start-1]
        
        return ans