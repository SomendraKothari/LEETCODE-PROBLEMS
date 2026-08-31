# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root,mn,mm):
        if not root:
            return True
        if root.val<mn or root.val>mm:
            return False
        cl=self.check(root.left,mn,root.val-1)
        cr=self.check(root.right,root.val+1,mm)
        return cl and cr
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check(root,-10000000000,10000000000)