# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:return None
        if left==right: return head
        dummy=ListNode(0,head)
        RealPrev=dummy
        curr=head
        for i in range(left-1):
            RealPrev=curr
            curr=curr.next
        prev=None
        for i in range((right-left)+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        RealPrev.next.next=curr
        RealPrev.next=prev
        return dummy.next