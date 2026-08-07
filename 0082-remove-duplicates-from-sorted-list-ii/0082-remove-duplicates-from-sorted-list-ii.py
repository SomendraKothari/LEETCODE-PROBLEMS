# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, h):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode()
        d.next=h
        c=d
        while h:
            if h.next and h.val==h.next.val:
                while h.next and h.val==h.next.val:
                    h=h.next
                c.next=h.next
            else:
                c=c.next
            h=h.next
        return d.next