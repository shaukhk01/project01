class Test:
    a = 10
    def __init__(self):
        self.b = 20
t1 = Test()
t2 = Test()
print(t1.a,t2.b)
Test.a = 100
print(t2.a)
t1.a = 200
print(t1.a)
print(t2.a)
Test.b = 300
print(Test.__dict__)
