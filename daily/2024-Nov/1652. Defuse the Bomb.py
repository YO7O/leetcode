class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        ans = [0] * len(code)

        if k < 0:
            cursum = sum(code[len(code)+k:])
            for i in range(len(code)):
                ans[i] = cursum
                cursum += code[i] - code[i+k]
            return ans
        
        if k > 0:
            cursum = sum(code[len(code)-k:])
            for i in range(-k-1, len(code)-k-1):
                ans[i] = cursum
                cursum += code[i+k+1] - code[i+1]
            return ans

        return ans