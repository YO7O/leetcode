class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.strip().split(" ")
        ans = ""
        print(array)
        for i in range(len(array)-1, -1, -1):
            if array[i]:
                ans += array[i] + " "
        ans = ans[:-1]
        return ans