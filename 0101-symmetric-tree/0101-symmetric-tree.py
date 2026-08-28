# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class que():
    def __init__(self):
        self.q=[]
        self.f=-1
    def push(self,x):
        if self.f==-1:
            self.f=0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x=self.q[self.f]
        self.f+=1
        if self.f==len(self.q):
            self.f=-1
            self.q=[]
        return x
    def size(self):
        if self.f==-1:
            return 0
        return len(self.q)-self.f
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        q=que()
        q.push(root)
        while q.size()>0:
            l=q.size()
            le=[]
            for i in range(l):
                x=q.pop()
                if x.left:
                    q.push(x.left)
                    le.append(x.left.val)
                else:
                    le.append(101)
                if x.right:
                    q.push(x.right)
                    le.append(x.right.val)
                else:
                    le.append(101)
            lle=len(le)
            for i in range(lle//2):
                if le[i]!=le[-i-1]:
                    return False
        return True