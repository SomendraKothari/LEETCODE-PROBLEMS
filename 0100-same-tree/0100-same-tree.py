# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        ans=[]
        def pre(r):
            if not r:
                ans.append(None)
                return
            ans.append(r.val)
            pre(r.left)
            pre(r.right)
        pre(p)
        pre(q)
        l=len(ans)
        return ans[:l//2]==ans[l//2:]