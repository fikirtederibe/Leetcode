class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for j,n in enumerate(nums):
            nums[j]= str(n)
        def compare(c1,c2):
            if c1+c2 > c2+c1:
                return -1
            else:
                return 1
        nums= sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))