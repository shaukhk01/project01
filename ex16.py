class X:
    a = 10
    def __init__(self):
        self.b = 20
    @staticmethod
    def main():
        print('method of x class')
class Y:
    c = 30
    def __init__(self):
        self.d = 40
    @staticmethod
    def main1():
        print('method of class Y')
    def m2(self):
        x1 = X()
        x1.main()
        print(x1.a)
        print(x1.b)
        print(self.d)
        print(self.c)
y1 = Y()
y1.m2()
