class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = {c: s.count(c) for c in 'abc'}
        if any(counts[c] < k for c in counts):
            return -1
        
        start = 0
        n = len(s)
        m = 0
        for end in range(n):
            counts[s[end]] -= 1
            while counts[s[end]] < k:
                counts[s[start]] += 1
                start += 1
            m = max(m, end-start+1)
        return n-m