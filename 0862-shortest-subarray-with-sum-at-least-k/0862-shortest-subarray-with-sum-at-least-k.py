class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum=[0]
        mini=float(inf)
        for n in nums:
            prefix_sum.append(prefix_sum[-1]+n)
        deque = collections.deque()
        for indx,curr in enumerate(prefix_sum):
            while deque and deque[-1][1]>=curr:
                deque.pop()
            while deque and curr-deque[0][1]>=k:
                mini=min(mini,indx-deque[0][0])
                deque.popleft()
            deque.append((indx,curr))
        return mini if mini!=float(inf) else-1