class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals)==1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        res=[]

        for interval in intervals:
            if not res or interval[0]>res[-1][1]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1],interval[1])

        return res

