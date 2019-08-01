class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def main(self):
        print(Test.a)
    @classmethod
    def m1(cls):
        print(cls.a)
    @staticmethod
    def m2():
        print(Test.a)
c = Test()
c.main()
c.m1()
c.m2()
print(c.a)
