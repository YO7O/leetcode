class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = [(ps / total - (ps + 1) / (total + 1), ps, total) for ps, total in classes]
        heapify(diff)

        while extraStudents > 0:
            d, ps, total = diff[0]
            ps += 1
            total += 1
            heapreplace(diff, (ps / total - (ps + 1) / (total + 1), ps, total))
            extraStudents -= 1
        
        return sum(ps / total for d, ps, total in diff) / len(classes)