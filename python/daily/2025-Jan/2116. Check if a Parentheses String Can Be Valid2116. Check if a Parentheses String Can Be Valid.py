class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        unlock = lock = 0
        for i in range(n):
            if locked[i] == "0":
                unlock += 1
                continue

            if s[i] == "(":
                lock += 1
            else:
                lock -= 1
                if unlock + lock < 0:
                    return False

        unlock = lock = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == "0":
                unlock += 1
                continue

            if s[i] == ")":
                lock += 1
            else:
                lock -= 1
                if unlock + lock < 0:
                    return False

        return True
