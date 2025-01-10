class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        changes = [0] * (n + 1)

        for start, end, direction in shifts:
            d = 1 if direction else -1
            changes[start] += d
            changes[end+1] += -d
        
        array = list(s)
        cur = 0
        a = ord('a')
        for i in range(n):
            cur += changes[i]
            array[i] = chr((ord(array[i]) + cur - a) % 26 + a)
            
        return "".join(array)