class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        st=[]
        for i,n in enumerate(temperatures):
            while st and temperatures[st[-1]]<n:
                prev_indx=st.pop()
                answer[prev_indx]=i-prev_indx
                
            st.append(i)
        return answer
        