class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        string_x=str(x)
        if string_x[0]=='-':
            flag=1
            string_x=string_x[1:]
        string_x=string_x[::-1]
        int_x=int(string_x)
        if flag==1:
            int_x=-int_x
        return int_x if (int_x >= -2**31) and (int_x <= (2**31)-1) else 0