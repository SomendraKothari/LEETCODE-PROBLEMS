class Solution(object):
    def totalFruit(self, f):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # s=set()
        # l=0
        # m=0
        # for r in range(len(f)):
        #     s.add(f[r])
        #     if len(s)>2:
        #         m=max(m,r-l)
        #         l=r-1
        #         while f[l]==f[l-1]:
        #             l-=1
        #         s.discard(f[l-1])
        # if m<len(f)-l:
        #     m=len(f)-l
        # return m
        in1=in2=-1
        v1=v2=None
        l=0
        m=0
        for r in range(len(f)):
            if v1==f[r]:
                in1=r
            elif v2==f[r]:
                in2=r
            elif v1==None:
                v1,in1=f[r],r
            elif v2==None:
                v2,in2=f[r],r
            else:
                m=max(r-l,m)
                if in1<in2:
                    l=in1+1
                    v1,in1=f[r],r
                else:
                    l=in2+1
                    v2,in2=f[r],r
        m=max(len(f)-l,m)
        return m