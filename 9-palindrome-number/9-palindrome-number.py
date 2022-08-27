class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        k=(len((x))//2)
        i=0
        flag=0
        n=len((x))-1
        if x.count(x[0]) == len(x):
                return True
        while(i<k and n>=k):
            if x[i]!=x[n]:
                flag=1
            i=i+1
            n=n-1
        return False if flag else True