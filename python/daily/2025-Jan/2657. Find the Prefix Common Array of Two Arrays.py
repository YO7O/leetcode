class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        waitA, waitB = [False] * (n + 1), [False] * (n + 1)
        ans, cur = [0] * n, 0
        
        for i in range(n):
            if waitA[B[i]]:
                waitA[B[i]] = False
                cur += 1
            else:
                waitB[B[i]] = True
            
            if waitB[A[i]]:
                waitB[A[i]] = False
                cur += 1
            else:
                waitA[A[i]] = True
            ans[i] = cur
        
        return ans