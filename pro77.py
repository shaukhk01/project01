def main():
    class p1:
        def m1(self):
            print('parent class method.')
    class p2(p1):
        def m2(self):
            print('child class method.')
    class p3(p1):
        def m3(self):
            print('child2 class method')
    c = p3()
    c.m1()
    c.m3()
    d = p2()
    d.m1()
    d.m2()
main()

