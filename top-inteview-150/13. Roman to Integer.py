class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        for i in range(len(s)):
            match s[i]:
                case 'I':
                    if i < len(s)-1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                        value -= 1
                    else:
                        value += 1
                case 'V':
                    value += 5
                case 'X':
                    if i < len(s)-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                        value -= 10
                    else:
                        value += 10
                case 'L':
                    value += 50
                case 'C':
                    if i < len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                        value -= 100
                    else:
                        value += 100
                case 'D':
                    value += 500
                case 'M':
                    value += 1000
        return value