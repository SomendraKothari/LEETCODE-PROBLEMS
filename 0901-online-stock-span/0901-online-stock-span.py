class StockSpanner(object):

    def __init__(self):
        self.sa=[]

    def next(self, p):
        """
        :type price: int
        :rtype: int
        """
        c=1
        while self.sa and self.sa[-1][0]<=p:
                pp,pc=self.sa.pop()
                c+=pc
        self.sa.append((p,c))
        return c 
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)