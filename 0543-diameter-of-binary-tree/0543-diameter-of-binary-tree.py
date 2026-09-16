# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.m=[]
    def h(self,root):
        if not root:
            return 0
        l=self.h(root.left)
        r=self.h(root.right)
        self.m.append(l+r)
        if l>r:
            return l+1
        return r+1
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        l=self.h(root)
        return max(self.m)