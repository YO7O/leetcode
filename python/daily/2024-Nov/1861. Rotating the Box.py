class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        ans = [['.'] * m for _ in range(n)]
        for i in range(m):
            k = n-1
            l = m-1-i
            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    ans[k][l] = '#'
                    k -= 1
                elif box[i][j] == '*':
                    ans[j][l] = '*'
                    k = j-1
        return ans