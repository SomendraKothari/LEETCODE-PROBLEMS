# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, a, b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # l1=0
        # c=a
        # while c:
        #     l1+=1
        #     c=c.next
        # l2=0
        # c2=b
        # while c2:
        #     l2+=1
        #     c2=c2.next
        # if l1<l2:
        #     cur=a
        #     for _ in range(l1):
        #         bu=b
        #         while bu:
        #             if cur==bu:
        #                 return cur
        #             bu=bu.next
        #         cur=cur.next 
        # else:
        #     cur=b
        #     for _ in range(l2):
        #         bu=a
        #         while bu:
        #             if cur==bu:
        #                 return cur
        #             bu=bu.next
        #         cur=cur.next
        # return None
        # tle ho gya

        # l1=0
        # c=a
        # while c:
        #     l1+=1
        #     c=c.next
        # l2=0
        # c2=b
        # while c2:
        #     l2+=1
        #     c2=c2.next
        # if l1<l2:
        #     for _ in range(l2-l1):
        #         b=b.next
        # else:
        #     for _ in range(l1-l2):
        #         a=a.next
        # while a:
        #     if a==b:
        #         return a
        #     a=a.next
        #     b=b.next
        # return None

        x=a
        y=b
        c=0
        while True:
            if x==y:
                return x
            x=x.next
            y=y.next
            if x==None:
                x=b
                c+=1
            if y==None:
                y=a
            if c>1:
                return None