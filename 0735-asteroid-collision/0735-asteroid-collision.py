class Solution(object):
    def asteroidCollision(self, sa):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s=[]
        for a in sa:
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
                s.append(a)
        return s