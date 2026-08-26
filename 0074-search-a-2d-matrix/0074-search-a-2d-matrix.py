class Solution(object):
    def searchMatrix(self, m, t):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nr=len(m)
        nc=len(m[0])
        l=0
        r=nr*nc-1
        while l<=r:
            mi=(l+r)//2
            el=m[mi//nc][mi%nc]
            if el==t:
                return True
            elif el<t:
                l=mi+1
            else:
                r=mi-1
        return False