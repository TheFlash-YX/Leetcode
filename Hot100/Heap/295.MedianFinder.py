import heapq
class MedianFinder:

    def __init__(self):
        # 用来存较小的部分数据，大顶堆，用负数存储
        self.min=[]
        # 用来存放较大的部分数据
        self.max=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min,-num)
        heapq.heappush(self.max,-heapq.heappop(self.min))

        if len(self.max)>len(self.min):
            heapq.heappush(self.min,-heapq.heappop(self.max))

    def findMedian(self) -> float:
        if len(self.min)>len(self.max):
            return float(-self.min[0])
        else:
            return (-self.min[0]+self.max[0])/2.0