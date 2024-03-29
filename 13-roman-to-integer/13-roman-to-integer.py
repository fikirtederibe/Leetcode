class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        output=0
        i=0
        while i<len(s):
            if i+1<len(s) and dict[s[i]]<dict[s[i+1]]:
                output-=dict[s[i]]
            else:
                output+=dict[s[i]]
            i+=1
        return output
            