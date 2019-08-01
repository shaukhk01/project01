class p:
    def m1(self):
        print('parent class method.')
class c(p):
    def m2(self):
        print('child class method.')
c = c()
c.m1()
c.m2()
