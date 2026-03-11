from string import digits
from typing import List
class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result=[]
        self.s=""

    def backtracking(self,digits,index):
        if len(digits)==index:
            self.result.append(self.s)
            return

        digit=int(digits[index])
        letter=self.letterMap[digit]

        for i in range(len(letter)):
            self.s+=letter[i]
            self.backtracking(digits,index+1)
            self.s=self.s[:-1]



    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.backtracking(digits,0)
        return self.result
