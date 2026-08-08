class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x==0:
        #     return 0
        # i=1
        # while i*i<=x:
        #     i+=1
        # return i-1
        # code shi h tle ho rha h
        if x<2:
            return x
        l=0
        r=x
        a=0
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            if m*m>x:
                r=m-1
            elif m*m<x:
                a=m
                l=m+1
        return a