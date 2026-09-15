# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pre(self,r):
        if not r:
            return
        r.right,r.left=r.left,r.right
        self.pre(r.right)
        self.pre(r.left)
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        self.pre(root)
        return root