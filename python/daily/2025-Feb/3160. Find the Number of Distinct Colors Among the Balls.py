class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Counter() is weirdly slow, probably due to older version of python is used
        # https://stackoverflow.com/questions/27801945/surprising-results-with-python-timeit-counter-vs-defaultdict-vs-dict
        count = {}
        balls = {}
        distinct = 0
        ans = [0] * len(queries)

        for i, (ball, label) in enumerate(queries):
            if ball in balls:
                oldLabel = balls[ball]
                count[oldLabel] -= 1
                if count[oldLabel] == 0:
                    del count[oldLabel]
                    distinct -= 1
            
            if label not in count:
                distinct += 1
                count[label] = 1
            else:
                count[label] += 1
            balls[ball] = label
            ans[i] = distinct

        return ans