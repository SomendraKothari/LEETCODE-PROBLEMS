class Solution(object):
    def merge(self,n,l,m,r):
        sa,sasa=[],[]
        for i in range(l,m+1):
            sa.append(n[i])
        for i in range(m+1,r+1):
            sasa.append(n[i])
        i,j,k=0,0,l
        lsa=len(sa)
        lsasa=len(sasa)
        while k<=r:
            if i==lsa:
                n[k]=sasa[j]
                j+=1
            elif j==lsasa:
                n[k]=sa[i]
                i+=1
            elif sa[i]<sasa[j]:
                n[k]=sa[i]
                i+=1
            else:
                n[k]=sasa[j]
                j+=1
            k+=1

    def ms(self,n,l,r):
        if l>=r:
            return 
        m=(l+r)//2
        self.ms(n,l,m)
        self.ms(n,m+1,r)
        self.merge(n,l,m,r)
    def sortArray(self, n):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.ms(n,0,len(n)-1)
        return n