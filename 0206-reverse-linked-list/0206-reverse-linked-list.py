# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self,c,n,p):
        if c==None:
            return p
        n=c.next
        c.next=p
        return self.rev(n,n,c)
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # p=n=None
        # c=head
        # while c:
        #     n=c.next
        #     c.next=p
        #     p=c
        #     c=n
        # return p

        return self.rev(head,None,None)

