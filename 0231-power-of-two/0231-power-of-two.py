class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        else:
            power_=1
            while power_<n:
                power_*=2
            if power_==n:
                return True
            return False
        