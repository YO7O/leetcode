class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        j = 0
        for i in range(n):
            if (ord(str2[j]) - ord(str1[i])) % 26 <= 1:
                j += 1
                if j >= m:
                    return True

        return False