class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[]
        for values in nums:
            a.append(int(values))
        a.sort(reverse=True)
        return str(a[k-1])
            
        