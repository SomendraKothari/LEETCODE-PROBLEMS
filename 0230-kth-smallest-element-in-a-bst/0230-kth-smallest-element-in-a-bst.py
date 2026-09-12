# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.a=None
        self.k=k
        def ino(root):
            if not root or self.a:
                return
            ino(root.left)
            self.k-=1
            if self.k==0:
                self.a=root.val
                return
            ino(root.right)
        ino(root)
        return self.a