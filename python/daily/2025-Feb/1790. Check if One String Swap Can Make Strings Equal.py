class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        unmatched = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unmatched.append(i)
        if not unmatched:
            return True
        if len(unmatched) != 2 or s1[unmatched[0]] != s2[unmatched[1]] or s1[unmatched[1]] != s2[unmatched[0]]:
            return False
        return True