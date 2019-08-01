class parent:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('parent method')
    def m2(cls):
        print('parent class')
    @staticmethod
    def m3():
        print('parent static')
class child(parent):
      o.m1()
o = child()
print(o.a,o.b)
o.m2()
o.m3()
