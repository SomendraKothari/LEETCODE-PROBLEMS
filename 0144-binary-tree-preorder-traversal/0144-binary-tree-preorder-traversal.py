# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rec(self,root,ans):
        if root==None:
            return
        ans.append(root.val)
        self.rec(root.left,ans)
        self.rec(root.right,ans)

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans=[]
        self.rec(root,ans)
        return ans