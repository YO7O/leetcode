class Solution:
    def __init__(self):
        self.prime = [True] * 1001

    def sieve(self, max) -> None:
        self.prime[0] = False
        self.prime[1] = False
        for i in range(2, ceil(sqrt(max))+1):
            if self.prime[i]:
                for j in range(i*i, max, i):
                    self.prime[j] = False

    def primeSubOperation(self, nums: List[int]) -> bool:
        self.sieve(1001)
        primeNum = []
        for i in range(2, len(self.prime)):
            if self.prime[i]:
                primeNum.append(i)

        for i in range(len(nums)-2, -1, -1):
            # can do binary search on primeNum to do O(nlogp) instead of O(np)
            if nums[i] >= nums[i+1]:
                ppos = 0
                while ppos < len(primeNum) and primeNum[ppos] <= nums[i]-nums[i+1] and primeNum[ppos] < nums[i]:
                    ppos += 1
                
                if ppos == len(primeNum) or primeNum[ppos] >= nums[i]:
                    return False
                nums[i] -= primeNum[ppos]
                ppos += 1

        return True