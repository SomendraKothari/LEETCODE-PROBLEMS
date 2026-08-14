class Solution(object):
    def nextGreaterElements(self, n):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n+=n
        # l=len(n)
        # s=[]
        # ans=[-1]*l
        # for i in range(l):
        #     while s and n[s[-1]]<n[i]:
        #         ind=s.pop()
        #         ans[ind]=n[i]
        #     s.append(i)
        # return ans[:l//2]


        l=len(n)
        ans=[-1]*l
        s=[]
        for i in range(2*l):
            j=i%l
            while s and n[s[-1]]<n[j]:
                ind=s.pop()
                ans[ind]=n[j]
            s.append(j)
        return ans