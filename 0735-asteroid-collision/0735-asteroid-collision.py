class Solution(object):
    def asteroidCollision(self, sa):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s=[sa[0]]
        for i in range(1,len(sa)):
            a=sa[i]
            c=1
            if a<0:
                while s and s[-1]>0:
                    if -a>s[-1]:
                        s.pop()
                    elif -a==s[-1]:
                        s.pop()
                        c=0
                        break
                    else:
                        c=0
                        break
            if c==1:
                s.append(sa[i])
        return s