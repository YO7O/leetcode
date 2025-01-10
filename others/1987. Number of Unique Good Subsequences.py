class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 1000000007
        zeros, ones, haszero = 0, 0, 0

        for d in binary:
            if d == '0':
                haszero = 1
                zeros = (zeros + ones) % mod
            else:
                ones = (zeros + ones + 1) % mod
        
        return (zeros + ones + haszero) % mod
