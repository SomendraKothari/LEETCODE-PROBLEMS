class Solution(object):
    def maxFrequency(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n.sort()
        l=0
        s=0
        m=0
        for r in range(1,len(n)):
            if n[r]==n[r-1]:
                if m<r-l+1:
                    m=r-l+1
                continue
            s+=(n[r]-n[r-1])*(r-l)
            # print(s,r)
            if s==k:
                if m<r-l+1:
                    m=r-l+1
            while l<r and s>k:
                s-=n[r]-n[l]
                l+=1
                # print(2)
        if m<len(n)-l:
            # print(1)
            m=len(n)-l
        return m