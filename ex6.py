class P:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Instance method..')
    @classmethod
    def m2(cls):
        print('Class method..')
    @staticmethod
    def m3():
        print('Static method..')
class C(P):
    pass
obj = P()
obj.m1()
obj.m2()
obj.m3()
