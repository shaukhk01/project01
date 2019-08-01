class X:
    a = 10
    def __init__(self):
          self.b = 20
    def m1(self):
          print('class x method')
class Y:
    def m2(self):
        print('class y method.')
        x1 = X()
        x1.m1()
        print(x1.a)
o = Y()
o.m2()
