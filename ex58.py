class p:
    a = 10
    def __init__(self):
        self.b = 20
class C(p):
    c = 30
    def main(self):
        print(self.a)
        print(self.c)
        print(self.b)
c = C()
c.main()
