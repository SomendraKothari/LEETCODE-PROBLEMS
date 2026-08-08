# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        n=p=None
        while s:
            n=s.next
            s.next=p
            p=s
            s=n
        while p:
            if head.val!=p.val:
                return False
            head=head.next
            p=p.next
        return True