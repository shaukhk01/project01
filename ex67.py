class Test:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        self.a = 888
        self.b = 999
t1 = Test()
t2 = Test()
t1.m1()
print(t1.a)
print(t1.b)
print(Test.a)
