class Solution(object):
    def minEatingSpeed(self, p, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        r=max(p)
        while l<=r:
            m=(l+r)//2
            rh=0
            for i in p:
                rh+=(i-1)//m+1
            if rh<=h:
                r=m-1
            else:
                l=m+1
        return l