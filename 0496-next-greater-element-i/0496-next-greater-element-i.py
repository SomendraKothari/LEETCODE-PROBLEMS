class Solution(object):
    def nextGreaterElement(self, n1, n2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(n1)
        sa=[]
        ans=[-1]*n
        d={}
        for i in range(len(n2)):
            while sa and n2[sa[-1]]<n2[i]:
                ind=sa.pop()
                d[n2[ind]]=n2[i]
            sa.append(i)
        for i in range(n):
            ans[i] = d.get(n1[i],-1)
        return ans