def main():
    class super:
        a = 100
        def __init__(self,z):
            self.x = 10
            self.b = 20
            self.z = z
        def m1(self):
            print('super class method')
    class sub(super):
        a = 200
        def __init__(self):
            super().__init__()
        def m2(self):
            print('sub class method')
            print(self.a)
            print(self.b)
            super().m1()
            print(super().a)
            print(super().x)
            print(super().b)
    p = super(10)
    o = sub()
    o.m2()
main()
