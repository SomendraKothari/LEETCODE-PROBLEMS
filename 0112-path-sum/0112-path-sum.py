# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, t):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        self.ans=False
        def check(root,s):
            if self.ans:
                return
            if not root:
                return 0
            s+=root.val
            print(s,root.val)
            l=check(root.left,s)
            r=check(root.right,s)
            if l==0 and r==0 and s==t:
                self.ans=True
                return 0
        check(root,0)
        return self.ans