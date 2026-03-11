class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            pre_min=self.stack[-1][1]
            cur_min=min(val,pre_min)
            self.stack.append((val,cur_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

