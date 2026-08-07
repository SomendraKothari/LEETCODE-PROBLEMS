# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        l=1
        c=head
        while c.next:
            c=c.next
            l+=1
        k%=l
        if k==0:
            return head
        s=f=head
        for _ in range(k):
            f=f.next
        while f.next:
            s=s.next
            f=f.next
        f.next=head
        head=s.next
        s.next=None
        return head