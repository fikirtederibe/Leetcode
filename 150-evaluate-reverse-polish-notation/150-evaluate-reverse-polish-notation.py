from curses.ascii import isdigit
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        if not tokens:
            return 0
        for token in tokens:
            if token not in '+-*/':
                st.append(token)
            else:
                a=st.pop()
                b=st.pop()
                st.append(int(eval(str(b)+token+str(a))))
        return int(st.pop())
       
        