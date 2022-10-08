class MyStack:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]
        self.size=0
    def push(self, x: int) -> None:
        self.queue1.insert(0,x)
        self.size+=1
    def pop(self) -> int:
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.size-=1
        return self.queue2.pop()
    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        return self.queue2[-1]
    def empty(self) -> bool:
        return self.size==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()