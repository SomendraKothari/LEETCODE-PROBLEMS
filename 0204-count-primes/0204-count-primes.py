class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        l=[1]*(n)
        l[0]=l[1]=0
        for i in range(2,int(n**0.5)+1):
            if l[i]:
                for j in range(i*i,n,i):
                    l[j]=0
        return sum(l)