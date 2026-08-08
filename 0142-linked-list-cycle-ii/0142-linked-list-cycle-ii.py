# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s=f=head
        cycle=False
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f:
                cycle = True
                break
        if cycle==False:
            return None
        l=1
        while s.next!=f:
            s=s.next
            l+=1
        s=f=head
        for _ in range(l):
            f=f.next
        while s!=f:
            s=s.next
            f=f.next
        return s