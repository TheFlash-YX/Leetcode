from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        alloc=[1]*len(ratings)
        #从前向后，确定右孩子>左孩子的情况
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1]:
                alloc[i+1]=alloc[i]+1
        #从后向前，确定左孩子>右孩子的情况
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i]:
                #要取二者中的最大值，才能保证同时比左边多且比右边多
                alloc[i-1]=max(alloc[i]+1,alloc[i-1])


        return sum(alloc)


if __name__ =="__main__":
    ratings=[1,2,87,87,87,2,1]
    solution=Solution()
    result=solution.candy(ratings)
    print(result)

