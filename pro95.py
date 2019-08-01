def main():
    class p1:
        def __init__(self):
            self.m1()
        def m1(self):
            print('p1 class method.')
    class p2(p1):
        def __init__(self):
            self.m2()
            super().__init__()
        def m2(self):
            print('p2 class method.')
    class p3(p2):
        def __init__(self):
            self.m3()
            super().__init__()
        def m3(self):
            print('p3 class method.')
    o = p3()
main()
