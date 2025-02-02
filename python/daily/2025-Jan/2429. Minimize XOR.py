class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = num2.bit_count()

        positive, negative = deque([]), deque([])
        cur = 1
        while num1 > 0:
            if num1 % 2 == 1:
                positive.append(cur)
            else:
                negative.append(cur)
            if len(positive) + len(negative) > bits:
                if negative:
                    negative.pop()
                else:
                    positive.popleft()
            cur *= 2
            num1 //= 2

        while len(positive) + len(negative) < bits:
            negative.append(cur)
            cur *= 2

        return sum(positive) + sum(negative)
