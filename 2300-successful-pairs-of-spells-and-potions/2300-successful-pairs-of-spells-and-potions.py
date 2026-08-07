class Solution(object):
    def successfulPairs(self, sp, p, s):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n=len(sp)
        m=len(p)
        p.sort()
        ans=[0]*n
        for i in range(n):
            if i>0 and sp[i]==sp[i-1]:
                ans[i]=ans[i-1]
                continue
            c=sp[i]
            l=0
            r=m-1
            while l<=r:
                mi=(r+l)//2
                if c*p[mi]<s:
                    l=mi+1
                else:
                    r=mi-1
            ans[i]=m-l
        return ans