class Solution(object):
    def totalFruit(self, f):
        """
        :type fruits: List[int]
        :rtype: int
        """
        s=set()
        l=0
        m=0
        for r in range(len(f)):
            s.add(f[r])
            if len(s)>2:
                m=max(m,r-l)
                l=r-1
                while f[l]==f[l-1]:
                    l-=1
                s.discard(f[l-1])
        if m<len(f)-l:
            m=len(f)-l
        return m