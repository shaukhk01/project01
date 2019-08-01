class parent:
    a = 20
    def __init__(self,name,deptno):
        self.name = name
        self.deptno = deptno
    def main(self):
        print('parent class')
class child:
    def m2(self):
        print('child class')
        sub = parent('ANNIE',20)
        sub.main()
        print(self.sub.a)

o = child()
o.m2()
