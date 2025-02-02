class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsTable = {}
        for word in words:
            wordsTable[word] = 1 if word not in wordsTable else wordsTable[word] + 1
        wordCount = len(wordsTable)
        
        n, m = len(s), len(words[0])
        ans = []

        for i in range(m):
            start = i
            curWC = wordCount
            for j in range((n - i) // m):
                pos = j * m + i
                word = s[pos:pos+m]
                if word not in wordsTable:
                    while start < pos:
                        w = s[start:start+m]
                        if w in wordsTable:
                            wordsTable[w] += 1
                        start += m
                    curWC = wordCount
                    start += m
                    continue

                if wordsTable[word] == 0:
                    while wordsTable[word] == 0:
                        w = s[start:start+m]
                        if w in wordsTable:
                            wordsTable[w] += 1
                            if wordsTable[w] == 1:
                                curWC += 1
                        start += m
                    wordsTable[word] -= 1
                    if wordsTable[word] == 0:
                        curWC -= 1
                    continue


                wordsTable[word] -= 1
                if wordsTable[word] == 0:
                    curWC -= 1
                    if curWC == 0:
                        ans.append(start)
                        w = s[start:start+m]
                        wordsTable[w] += 1
                        curWC += 1
                        start += m
                        
            while start < n:
                w = s[start:start+m]
                if w in wordsTable:
                    wordsTable[w] += 1
                start += m

        return ans