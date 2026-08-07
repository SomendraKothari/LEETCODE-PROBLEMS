class Solution(object):
    def shipWithinDays(self, w, d):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        if d==1:
            return sum(w)
        l=max(w)
        # r=max(sum(w)//d,sum(w)//2)
        r=sum(w)
        while l<r:
            m=(r+l)//2
            cw=0
            rd=1
            for i in w:
                if cw+i>m:
                    cw=0
                    rd+=1
                cw+=i
            if rd>d:
                l=m+1
            else:
                r=m
        return l