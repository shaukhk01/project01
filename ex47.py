class P:
    a = 10
    def __init__(self):
        self.b = 13
class C(P):
    def __init__(self):
        self.c = 20
        super().__init__()
    def main(self):
        print(self.b)
        print(super().a)
        print(self.c)
c = C()
c.main()

