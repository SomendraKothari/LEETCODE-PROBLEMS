class Solution(object):
    def calPoints(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        s=[]
        for i in range(len(o)):
            if o[i]=='+':
                m=int(s[-1]) + int(s[-2])
                s.append(m)
            elif o[i]=='D':
                s.append(int(s[-1])*2)
            elif o[i]=='C':
                s.pop()
            else:
                s.append(int(o[i]))
        return sum(s)