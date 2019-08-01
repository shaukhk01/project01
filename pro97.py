def main():
    class p:
        def __init__(self):
            self.c  = 'instance variable can\'t access another class instance method'
    class c(p):
        a = 200
        def __init__(self):
            self.b = 'child instance variable.'
            super().__init__()
            self.m1()
        def m1(self):
            print(self.b)
            print(self.c)
    o = c()
main()

