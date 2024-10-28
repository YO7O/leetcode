class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # spent 2 hours on a O(n) solution 
        # slower than O(n log n) solution 
        # OMEGALULIGUESS
        
        # O(n) solutionclass Solution:

            # constraint = 100001
            # lengthTable = [0] * constraint
            # leftTable = [-1] * constraint
            # rightTable = [-1] * constraint
            # ans = 0
            # for num in nums:
            #     if lengthTable[num]:
            #         continue
            #     right = num
            #     left = num
            #     length = 1

            #     rnum = num*num
            #     rnum = rnum if rnum < constraint else 0
            #     lnum = math.sqrt(num)
            #     lnum = int(lnum) if float(int(lnum)) == lnum else 0

            #     if rightTable[rnum] != -1:
            #         right = rightTable[rnum]
            #         length += lengthTable[rnum]
            #     if leftTable[lnum] != -1:
            #         left = leftTable[lnum]
            #         length += lengthTable[lnum]

            #     lengthTable[left] = length
            #     lengthTable[right] = length
            #     lengthTable[num] = length
            #     leftTable[right] = left
            #     leftTable[left] = left
            #     rightTable[left] = right
            #     rightTable[right] = right

            #     ans = max(length, ans)

            # return ans if ans != 1 else -1


        # O (n log n) solution
        table = {}
        nums.sort()
        ans = -1

        for num in nums:
            sq = math.sqrt(num)

            if sq * sq == num and sq in table:
                table[num] = table[sq]+1
                ans = max(ans, table[num])
            else:
                table[num] = 1

        return ans