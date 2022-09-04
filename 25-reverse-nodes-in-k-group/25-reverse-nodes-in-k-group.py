# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head
        prev = dummy = ListNode(0, head)
        while curr:
            count=count+1
            curr=curr.next
        if k>count or k<=0:
            return None
        for l in range(count//k):
            start=prev
            for i in range(k):
                head.next,head,prev=prev,head.next,head
                # head=head.next
                # prev=head
            start.next.next = head
            start.next, prev = prev, start.next
        return dummy.next
        