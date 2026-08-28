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
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        ans=[]
        if not root:
            return ans
        q=que()
        q.push(root)
        ans.append(float(root.val))
        while q.size()>0:
            l=q.size()
            le=0
            c=0
            for i in range(l):
                x=q.pop()
                if x.left:
                    q.push(x.left)
                    le+=x.left.val
                    c+=1
                if x.right:
                    q.push(x.right)
                    le+=x.right.val
                    c+=1
            if c>0:
                ans.append(float(le)/c)
        return ans