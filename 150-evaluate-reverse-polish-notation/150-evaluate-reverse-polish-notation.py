class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for k in tokens:
            if k=="+":
                stack.append(stack.pop()+stack.pop())
            elif k=="-":  
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif k=="*":
                stack.append((stack.pop())*(stack.pop()))
            elif k=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(k))
        return stack[0]