class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n, i = len(words), 0
        ans = []
        words.sort(key = lambda x: (len(x), x))
        
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans