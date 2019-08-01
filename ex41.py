class Test:
    a = 10
    c = 30
    @classmethod
    def main(cls):
        b = 20
        del cls.a
c = Test()
c.main()
print(Test.__dict__)
