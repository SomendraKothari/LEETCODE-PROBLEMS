class Solution(object):
    def findMaxConsecutiveOnes(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        m=0
        for r in range(len(n)):
            if n[r]==1:
                continue
            if m<r-l:
                m=r-l
            l=r+1
        m=max(len(n)-l,m) 
        return m