# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, h):
        """
        :type head: ListNode
        :rtype: bool
        """
        # l=set()
        # while h:
        #     if h in l:
        #         return True 
        #     l.add(h)
        #     h=h.next
        # return False
        s=h
        f=h
        while f and f.next: 
            s=s.next
            f=f.next.next
            if s==f:
                return True
        return False