class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.strip().split(' ')
        return len(array[-1])