class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dict_={num:i for i,num in enumerate(nums1)}
        output=[-1]*len(nums1)
        for i in range(len(nums2)):
            current=nums2[i]
            while stack and current>stack[-1]:
                val=stack.pop()
                indx=dict_[val]
                output[indx]=current
            if current in dict_:
                stack.append(current)
            else:continue
        return output
                
                