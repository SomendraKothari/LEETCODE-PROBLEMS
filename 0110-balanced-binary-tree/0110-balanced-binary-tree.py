# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=False
    def h(self,root):
        if not root:
            return 0
        a=self.h(root.left)
        s=self.h(root.right)
        if s>=a:
            h=s
            l=a
        else:
            h=a
            l=s
        if s!=a and (h-l)>1:
            self.ans=True
        return h+1
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.h(root)
        return not self.ans