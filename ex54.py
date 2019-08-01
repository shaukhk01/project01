class x:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('m1 method of class x')
class y:
    c = 30
    def __init__(self):
        self.d = 50
    def m2(self):
        print('m2 method of class y')
    def m3(self):
        x1 = x()
        x1.m1()
        print(x1.a)
        print(x1.b)
        self.m2()
        print(self.c)
        print(self.d)

c = y()
c.m3()
