from turtledemo.penrose import start
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum=0
        totalSum=0
        start=0
        for i in range(len(gas)):
            curSum+=gas[i]-cost[i]
            totalSum+=gas[i]-cost[i]
            if curSum<0:
                curSum=0
                start=i+1           #找出发点start

        if totalSum<0:              #保证总油量够用，能够完成循环
            return -1

        return start






