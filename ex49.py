class P:
    def __init__(self):
        self.b = 10
    def m1(self):
        self.b = 20
class C(P):
    def __init__(self):
        self.b = 30
        super().__init__()
        print(self.b)
        super().m1()
        print(self.b)
c = C()
