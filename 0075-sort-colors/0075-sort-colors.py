class Solution(object):
    # def part(self,n,l,r):
    #     key=n[r]
    #     st=l
    #     for i in range(l,r+1):
    #         if n[i]<=key:
    #             n[st],n[i]=n[i],n[st]
    #             st+=1
    #     return st-1

    # def qs(self,n,l,r):
    #     if l>=r:
    #         return
    #     p=self.part(n,l,r)
    #     self.qs(n,l,p-1)
    #     self.qs(n,p+1,r)
    # quick sort

    def sortColors(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # l=z=0
        # r=len(n)-1
        # while l<r:
        #     if n[l]==2:
        #         n[l],n[r]=n[r],n[l]
        #         while l<r and n[r]==2:
        #             r-=1
        #         # ab r waha jaha 0 ya 1
        #     elif n[l]==0:
        #         if l>z:
        #             n[l],n[z]=n[z],n[l]
        #             z+=1
        #         else:
        #             l+=1
        #     else:
        #         if n[r]==0:
        #             n[r],n[z]=n[z],n[r]
        #             z+=1
        #         else:
        #             l+=1
        # 2 pointer


        # l=len(n)
        # for i in range(l):
        #     for j in range(l-i-1):
        #         if n[j]>n[j+1]:
        #             n[j],n[j+1]=n[j+1],n[j]
        # return n
        # bubble sort

        # return self.qs(n,0,len(n)-1)
        # quick sort

        sa=[0]*(3)
        for i in n:
            sa[i]+=1
        j=0
        for i in range(3):
            while sa[i]>0:
                n[j]=i
                j+=1
                sa[i]-=1