class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.d= deque([])
    def insertFront(self, value: int) -> bool:
        if len(self.d)<self.k:
            self.d.appendleft(value)
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.d)<self.k:
            self.d.append(value)
            return True
        return False
    def deleteFront(self) -> bool:
        if self.d:
            self.d.popleft()
            return True
        return False
    def deleteLast(self) -> bool:
        if self.d:
            self.d.pop()
            return True
        return False
    def getFront(self) -> int:
        if self.d:
            return self.d[0]
        else:
            return -1
    def getRear(self) -> int:
        if self.d:
            return self.d[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if self.d:
            return False
        return True
    def isFull(self) -> bool:
        return len(self.d)==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()