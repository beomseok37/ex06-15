class example:
    data=[]
    def push(self,a):
        self.data.append(a)
    def printdata(self):
        for i in self.data:
            print(i)

e1=example()
e2=example()
e1.push(1)
e2.push(2)
print("e1")
e1.printdata()
print("e2")
e2.printdata()
