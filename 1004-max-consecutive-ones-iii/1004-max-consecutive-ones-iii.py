class Solution(object):
    def longestOnes(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # l=0
        # m=0
        # for r in range(len(n)):
        #     if n[r]==1:
        #         continue
        #     k-=1
        #     if k<0:
        #         if m<r-l:
        #             m=r-l
        #         while n[l]!=0:
        #             l+=1
        #         l+=1
        #         k+=1
        # m=max(len(n)-l,m)
        # return m

        # non shriking sw
        l=0
        for r in range(len(n)):
            if n[r]==0:
                k-=1
            if k<0:
                if n[l]==0:
                    k+=1
                l+=1
        return len(n)-l