class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        array = sorted([[num, pos] for pos, num in enumerate(nums)])

        sectionPos = [[array[0][1]]]
        for i in range(1, len(nums)):
            if array[i][0] - array[i-1][0] > limit:
                sectionPos.append([])
            sectionPos[-1].append(array[i][1])
        
        for sect in sectionPos:
            sect.sort()

        i = 0
        for sect in sectionPos:
            for pos in sect:
                nums[pos] = array[i][0]
                i += 1
            
        return nums