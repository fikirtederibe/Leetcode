class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair= sorted(zip(position, speed))
        stack=[]
        for pos,sp in (pair):
            time_=(target-pos)/sp
            if not stack:
                stack.append(time_)
            while stack and time_>=stack[-1]:
                stack.pop()
            stack.append(time_)
        return len(stack)
        