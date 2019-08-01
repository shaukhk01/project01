def main():
    class p:
        def m1(self):
            a = 'parent overriding'
    class p2(p):
        def m1(self):
            print(self.a)
    c = p2()
    c.m1()
main()
