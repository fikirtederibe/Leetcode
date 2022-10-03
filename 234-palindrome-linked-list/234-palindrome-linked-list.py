# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        k=head
        list_=[]
        while k:
            list_.append(k.val)
            k=k.next
        if list_==list_[::-1]:
            return True
        else:
            return False
            
        
        
        