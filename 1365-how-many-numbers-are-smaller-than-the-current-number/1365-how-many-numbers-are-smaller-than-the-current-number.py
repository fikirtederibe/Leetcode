class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        a=[]
        count=0
        for i in nums:
            for j in range(l):
               if (nums[j]-i)<0:
                   count+=1
            a.append(count)
            count=0
        return a


