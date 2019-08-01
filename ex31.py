class P:
    a = 10
    def __init__(self):
        self.b = 20
class C(P):
    c = 30
    def __init__(self):
        self.d = 40
        super().__init__()
o = C()
print(o.a,o.b,o.c,o.d)
