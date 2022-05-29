class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a = intervals[0]
        b = [a]
        for i in range(1, len(intervals)):
            if a[1] >= intervals[i][0] and a[1]<=intervals[i][1]:
                b[-1][1] = intervals[i][1] 
            elif intervals[i][0] >= a[1] :
                b.append(intervals[i])
            a = b[-1]
            
        return b
      