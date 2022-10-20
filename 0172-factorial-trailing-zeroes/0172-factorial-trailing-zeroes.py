class Solution:
    def trailingZeroes(self, n: int) -> int:
        j=5
        ans=0
        while j<=n:
            ans=ans+(n//j)
            j*=5
        return ans
        