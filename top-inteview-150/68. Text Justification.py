class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        curLine = 0
        start = 0
        s = ""
        ans = []
        for end in range(n):
            l = len(words[end])
            if curLine + l > maxWidth:
                if end - start == 1:
                    s = words[start] + " " * (maxWidth - len(words[start]))
                    start += 1
                else:
                    spaces = maxWidth - sum(len(word) for word in words[start:end])
                    avg = spaces // (end-start-1)
                    rmd = spaces % (end-start-1)
                    while start < end - 1:
                        spc = avg
                        if rmd > 0:
                            spc += 1
                            rmd -= 1
                        s += words[start] + " " * spc
                        start += 1
                    s += words[start]
                    start += 1
                ans.append(s)
                curLine = 0
                s = ""
            curLine += l + 1

        while start < n-1:
            s += words[start] + " "
            start += 1
        s += words[start]
        s += " " * (maxWidth - len(s))
        ans.append(s)

        return ans