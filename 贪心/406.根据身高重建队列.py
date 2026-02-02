from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #先按照身高排列
        people.sort(key=lambda x:(-x[0],x[1]))
        que=[]
        #再按照k排列
        for p in people:
            que.insert(p[1],p)

        return que