class MyQueue:

    def __init__(self):
       self.in_ =[]
       self.out =[]

    def push(self, x: int) -> None:
        self.in_.append(x)

    def pop(self) -> int:
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop())
        return self.out.pop()

    def peek(self) -> int:
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop())
        return self.out[-1]

    def empty(self) -> bool:
        if not self.in_ and not self.out:
            return True
        else:
             return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()