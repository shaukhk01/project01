def main():
    class p1:
        def m1(self):
            print('parent class method.')
    class p2(p1):
        def m2(self):
            print('child class method')
    o = p2()
    o.m1()
    o.m2()
main()
