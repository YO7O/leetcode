class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return k <= len(s) and k >= len([c for c in Counter(s).values() if c % 2 == 1])
