class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.mini_stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()