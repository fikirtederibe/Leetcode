class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        for i in range(len(l)):
            new_arr=nums[l[i]:r[i]+1]
            new_arr.sort()
            for i in range(1,len(new_arr)):
                #print(i)
                if(new_arr[1]-new_arr[0]==new_arr[i]-new_arr[i-1]):
                    flag=True
                else:
                    flag=False
                    break
            answer.append(flag)
        return answer
                    
                    
                
            
        