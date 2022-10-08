class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i,h in enumerate(heights):
            begin=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                begin=index
            stack.append((begin,h))
        for i,h in stack:
            max_area=max(max_area,h*(len(heights)-i))
        
        return max_area