# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        num = head
        count = 0
        while num:
            count+=1
            num = num.next
        node = (count - n)
        n = head
        i = 0
        if count <= 1:
            return None
        if node == 0:
            return head.next
        while n:
            i+=1
            if i == node:
                n.next = n.next.next
            n = n.next
        
        return head