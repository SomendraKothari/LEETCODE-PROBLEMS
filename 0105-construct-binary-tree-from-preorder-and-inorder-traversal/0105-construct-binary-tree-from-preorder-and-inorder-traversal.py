# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, p, i):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        l=len(p)
        d={}
        for ind,v in enumerate(i):
            d[v]=ind
        def r(p,ps,pe,i,iss,ie):
            if ps>pe or iss>ie:
                return None
            root=TreeNode(p[ps])
            ind=d[p[ps]]
            numsleft=ind-iss
            root.left=r(p,ps+1,ps+numsleft,i,iss,ind-1)
            root.right=r(p,ps+numsleft+1,pe,i,ind+1,ie)
            return root
        return r(p,0,l-1,i,0,l-1)