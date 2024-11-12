class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        q = sorted(enumerate(queries), key = itemgetter(1))
        items.sort(key = itemgetter(0))
        ans = [0] * len(queries)

        i = 0
        beauty = 0
        for key, query in q:
            while i < len(items) and query >= items[i][0]:
                beauty = max(beauty, items[i][1])
                i += 1
            ans[key] = beauty
            
        return ans