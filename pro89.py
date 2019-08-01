def main():
    class super:
        a = 10
        def __init__(self):
            self.b = 20
    class sub(super):
        def __init__(self):
            super.__init__(self)
            self.c = 40
        def main(self):
            print(self.c)
            print(self.a)
            print(self.b)
    o = sub()
    o.main()
main()

