# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output=ListNode(val=((l1.val+l2.val)%10))
        carry=(l1.val+l2.val)//10
        curr_node=output
        while(l1.next and l2.next):
            l1=l1.next
            l2=l2.next
            curr_node.next=ListNode(val=(l1.val+l2.val+carry)%10)
            carry=(carry+l1.val+l2.val)//10
            curr_node=curr_node.next
        while (l1.next):
            l1=l1.next
            curr_node.next=ListNode(val=((l1.val+carry)%10))
            carry=(carry+l1.val)//10
            curr_node=curr_node.next
        while (l2.next):
            l2=l2.next
            curr_node.next=ListNode(val=((l2.val+carry)%10))
            carry=(carry+l2.val)//10
            curr_node=curr_node.next
        if (carry)>0:
             curr_node.next= ListNode(val=1)
        return output
       
        
        