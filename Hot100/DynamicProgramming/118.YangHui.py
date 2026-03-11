from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]]
        for i in range(1,numRows):
            row=[1]*(i+1)
            pre_row = triangle[i - 1]
            for j in range(1,len(row)-1):
                row[j]=pre_row[j-1]+pre_row[j]
            triangle.append(row)

        return triangle

