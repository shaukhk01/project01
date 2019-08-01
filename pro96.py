def main():
    class p:
        a = 888
        def __init__(self):
            self.d = 10
    class c(p):
        a = 999
        def __init__(self):
            self.c = 200
            super().__init__()
            self.m1()
        def m1(self):
            print(self.a,self.c)
            print(super().a)
            print(self.d)
    o = c()
main()
