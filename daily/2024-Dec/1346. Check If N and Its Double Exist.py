class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = {}
        for num in arr:
            if num * 2 in table or num / 2 in table:
                return True
            table[num] = True
        return False