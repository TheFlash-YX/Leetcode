from collections import deque
class MyStack:

    def __init__(self):
        self.queue_in=deque()
        self.queue_out=deque()
    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.queue_out:
            return self.queue_out.popleft()
        else:
            for i in range(len(self.queue_in)-1):
                self.queue_out.append(self.queue_in.popleft())
            self.queue_out,self.queue_in=self.queue_in,self.queue_out
            return self.queue_out.popleft()


    def top(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_out, self.queue_in = self.queue_in, self.queue_out

        ans=self.queue_out.popleft()
        self.queue_in.append(ans)
        return ans


    def empty(self) -> bool:
        return len(self.queue_in)==0