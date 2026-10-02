# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, p):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        l=len(p)
        def r(ps,pe):
            if ps>pe:
                return None
            root=TreeNode(p[ps])
            t=pe
            while t>ps and p[t]>p[ps]:
                t-=1
            root.left=r(ps+1,t)
            root.right=r(t+1,pe)
            return root
        return r(0,l-1)