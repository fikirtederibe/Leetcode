class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-1
        arr=[]
        for i in range(len(nums)//2):
            result=nums[i]+nums[~i]
            arr.append(result)
        return max(arr)
          
        