class p1:
    def m1(self):
        print('parent class.')
class p2:
    def m2(self):
        print('child class')
class p3(p1,p2):
    def m3(self):
        print('sub class')
x = p3()
x.m1()
x.m2()
x.m3()
