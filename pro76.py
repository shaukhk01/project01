def main():
    class parent:
        def m1(self):
            print('parent class method.')
    class child(parent):
        def m2(self):
            print('child class method.')
    class sub(child):
        def m3(self):
            print('sub class method.')
    c = child()
    c.m1()
    print(issubclass(sub,child))
    print(isinstance(c,sub))
main()
