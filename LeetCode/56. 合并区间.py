class Solution:
    def merge(self, intervals: list) -> list:
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
