class Solution(object):
    def evalRPN(self, s):
        """
        :type tokens: List[str]
        :rtype: int
        """
        sa=[]
        for i in range(len(s)):
            if s[i]=='+':
                x=sa.pop()
                sa[-1]+=x
            elif s[i]=='-':
                x=sa.pop()
                sa[-1]-=x
            elif s[i]=='*':
                x=sa.pop()
                sa[-1]*=x
            elif s[i]=='/':
                x=sa.pop()
                y=sa[-1]
                sa[-1]=int(float(y)/x)
            else:
                sa.append(int(s[i]))
        return sa[-1]