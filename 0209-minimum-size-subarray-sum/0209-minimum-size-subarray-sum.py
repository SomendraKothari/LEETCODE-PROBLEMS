class Solution(object):
    def minSubArrayLen(self, t, n):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        s=0
        m=len(n)
        for r in range(len(n)):
            s+=n[r]
            if s<t:
                continue
            while s>=t:
                s-=n[l]
                l+=1
            if m>r-l+2:
                m=r-l+2
        return 0 if l==0 else m