class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output=[]
        for i in range(len(arr),1,-1):
            t=arr.index(max(arr[:i]))
            if t==i-1:
                continue
            else:
                arr=arr[t::-1]+arr[t+1:]
                output.append(t+1)
                arr=arr[i-1::-1]+arr[i:]
                output.append(i)
        return output
            
            