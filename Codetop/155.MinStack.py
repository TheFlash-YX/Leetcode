from math import inf


class MinStack:
    def __init__(self):
        self.st=[[0,inf]]

    def push(self,val:int)->None:
        self.st.append([val,min(val,self.st[-1][1])])

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1][0]


    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]