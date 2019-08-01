class Test:
    a = 10
    def __init__(self):
        self.b =20
    @classmethod
    def main(cls):
        cls.a = 100
        cls.b = 200
t1 = Test()
t2 = Test()
print(t1.a,t2.a)
t1.main()
print(t1.a,t2.a)
print(Test.__dict__)

print(Test.b)
print(t1.b)
