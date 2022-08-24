import sys
from itertools import count
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        if nums==0 or n==0:return 1
        have_one=0
        for i in range(n):
            if nums[i]==1:
                have_one=1
            elif nums[i]<=0 or nums[i]>n:
                nums[i]=1
        if have_one==0:return 1
        for i in range(n):
            dn= abs(nums[i])-1
            if nums[dn] >0:
                nums[dn]=-1*nums[dn]
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
            
        
               
        
         