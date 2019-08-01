class p:
    a = 888
    def m1(self):
        self.b = 10
class C(p):
    def m2(self):
        self.m1()
        print(self.b)
x = C()
x.m2()
