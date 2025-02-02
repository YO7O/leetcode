class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        arr.append(1000000000)
        arr.append(-1000000000)
        
        start = 0
        end = n
        ans = end

        while end > 0 and arr[end-1] <= arr[end]:
            end -= 1

        if end == 0:
            return 0

        while end <= n:
            while start < end and arr[start-1] <= arr[start] and arr[start] <= arr[end]:
                start += 1
            if arr[start-1] > arr[start]:
                return end - start
            end += 1
            start += 1

        return end - start