class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def main(self):
        Test.c = 30
    @classmethod
    def main1(cls):
        cls.d = 40
    @staticmethod
    def main2():
        Test.e = 50
obj = Test()
print(Test.__dict__)
obj.main()
obj.main1()
obj.main2()
Test.f = 100
print(Test.__dict__)
