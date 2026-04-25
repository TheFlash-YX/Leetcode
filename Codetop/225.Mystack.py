from collections import deque
class MyStack:

    def __init__(self):
        self.que=deque()

    def push(self, x: int) -> None:
        q=deque()
        while self.que:
            q.append(self.que.popleft())
        self.que.append(x)
        while q:
            self.que.append(q.popleft())

    def pop(self) -> int:
        return self.que.popleft()

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return False if self.que else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()