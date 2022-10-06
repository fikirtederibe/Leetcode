class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[]
        stack=[]
        for i in s:
            if i!=')':
                stack.append(i)
            else:
                while stack and stack[-1]!='(':
                    ans.append(stack[-1])
                    stack=stack[:-1]
                stack.pop()
                while ans:
                    stack.append(ans[0])
                    ans=ans[1:]
        return ''.join((stack))