class MinStack(object):

    def __init__(self):
        self.stack = []
        self.ms=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.ms or val<=self.ms[-1]:
            self.ms.append(val)


    def pop(self):
        """
        :rtype: None
        """
        v = self.stack.pop(-1)
        if self.ms[-1]==v:
            self.ms.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()