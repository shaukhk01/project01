def main():
    class p1:
        def m1(self):
            print('parent1 class method')
        class p2:
            def m2(self):
                print('parent2 class method')
        class p3(p1,p2):
            def m3(self):
                print('parent3 class method')
        o = p3()
        o.m1()
        o.m2()
        o.m3()
main()


