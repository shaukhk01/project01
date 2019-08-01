class Test:
    a = 10
    def m1(self):
        self.a = 99
    @classmethod
    def main(cls):
        cls.a = 100
    @staticmethod
    def m():
        Test.a = 200
print(Test.a)
Test.main()
print(Test.a)
o = Test()
o.m1()
print(o.a)
print(Test.a)
