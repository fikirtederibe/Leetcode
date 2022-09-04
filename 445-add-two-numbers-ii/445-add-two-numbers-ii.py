# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2=0,0
        while l1:
            n1=n1*10+l1.val
            l1=l1.next
        while l2:
            n2=n2*10+l2.val
            l2=l2.next
        sum=n1+n2
        curr=head=ListNode(0)
        if sum==0: return curr
        while sum:
            head.next=ListNode(sum%10,head.next)
            sum=sum//10
        return curr.next