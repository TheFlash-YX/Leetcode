from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0

        for bill in bills:
            if bill==5:
                five+=1

            if bill==10:
                ten+=1
                if five<=0:
                    return False
                else:
                    five-=1
            if bill==20:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                    twenty+=1
                else:
                    return False

        return True


