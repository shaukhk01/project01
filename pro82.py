class Engine:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Engine specific functionality.')
class car:
    def __init__(self):
        self.Engine = Engine()
    def m2(self):
        print('car using Engine class functionality.')
        print(self.Engine.a)
        print(self.Engine.a)
        self.Engine.m1()
o = car()
o.m2()

