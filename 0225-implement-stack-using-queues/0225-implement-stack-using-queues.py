class MyStack(object):

    def __init__(self):
        self.q1=[]
        self.q2=[]
        # self.f1=self.f2=-1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # if self.f1==-1:
        #     self.q1.append(x)
        #     self.f1=0
        # else:
        #     l1=len(self.q1)-self.f1#f1=3 f2=2 l1=2 l2=1
        #     # l2=len(self.q2)-self.f2
        #     # while self.f1<=l1:
        #     #     self.q2.append(self.q1[self.f1%l1])
        #     #     self.f1+=1
        #     for i in range(l1):
        #         self.q2.append(self.q1[self.f1%(l1+1)])
        #         self.f1+=1
        #     if self.f1>=l1:
        #         self.f2+=1
        #     self.q1.append(x)
        #     l2=len(self.q2)-self.f2
        #     for i in range(l2):
        #         self.q1.append(self.q2[self.f2%(l2+1)])
        #         self.f2+=1
        #     # self.f2-=1
        # print(self.q1,self.q2,self.f1,self.f2,"push")
        self.q2.append(x)

        # Step 2: q1 ke saare elements ko nikal kar (pop(0)) q2 mein daalo
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))

        # Step 3: q1 aur q2 ko swap kar do
        # Ab q1 mein saare elements Stack ke order (LIFO) mein aa chuke hain
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        """
        :rtype: int
        """
        # x=self.q1[self.f1]
        # self.f1+=1
        # if self.f1==len(self.q1):
        #     self.f1=-1
        # print(self.q1,self.q2,self.f1,self.f2,"pop")
        # return x
        return self.q1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        # print(self.q1,self.q2,self.f1,self.f2)
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        # print(self.q1,self.q2,self.f1,self.f2)
        return len(self.q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()