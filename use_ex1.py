from ex1 import Calc
class HouseKim:
    lastname="김"
    fullname=""
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print(self.fullname+", "+where+"로 여행을 가다.")
    def myname(self):
        print("내이름은 "+self.fullname+"입니다.")
    def __add__(self,other):
        print(self.fullname+"와(과) "+other.fullname+"이(가)결혼했습니다.")

class HouseHan(HouseKim):
    lastname="한"
    def travel(self,where,day):
        print(self.fullname+", "+where+"로 "+day+"일 여행을 가다.")
def add(a):
    return a+10
kim1=HouseKim("길동")
han1=HouseHan("둘리")
kim1+han1
c=Calc()
print(c.sum(3,4))
print(dir(HouseKim))
li=map(add,[1,2,3,4,5,6,7,8])
for i in li:
    print(i)
li2=map(lambda a,b:a+b,[1,2,3,4,5],[2,3,4,5,6])
for i in li2:
    print(i)
