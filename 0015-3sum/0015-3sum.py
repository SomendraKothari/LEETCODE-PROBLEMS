class Solution(object):
    def threeSum(self, n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n.sort()
        ans=[]
        # [-4,-1,-1,0,1,2]
        for i in range(len(n)):
            if i>0 and n[i]==n[i-1]:
                continue
            j=i+1
            k=len(n)-1
            while j<k:
                s=n[i]+n[j]+n[k]
                if s==0:
                    ans.append([n[i],n[j],n[k]])
                    while j<k and n[j]==n[j+1]:
                        j+=1
                    while j<k and n[k]==n[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        return ans