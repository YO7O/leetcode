class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a = ord('a')
        counter = [0] * 26
        for c in s:
            counter[ord(c)-a] += 1

        i = 25
        nxt = 24
        ans = ""
        while i >= 0:
            while nxt >= 0 and counter[nxt] == 0:
                nxt -= 1

            c = chr(i+a)

            if nxt == -1:
                return ans + c * min(repeatLimit, counter[i])

            if counter[i] > repeatLimit:
                ans += c * repeatLimit + chr(nxt+a)
                counter[i] -= repeatLimit
                counter[nxt] -= 1
            else:
                ans += c * min(repeatLimit, counter[i])
                counter[i] = 0
                i = nxt
                nxt = i - 1
            

        return ans